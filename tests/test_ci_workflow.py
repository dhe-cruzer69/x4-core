"""Regression tests ensuring CI failures cannot be silently ignored."""

from pathlib import Path
from typing import Any

import yaml

WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "ci.yml"
ALLOWED_QUALITY_COMMANDS = {
    "lint": {"python -m ruff check ."},
    "test": {"python -m pytest -q"},
}


def _load_workflow() -> dict[str, Any]:
    document = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    assert isinstance(document, dict), "CI workflow must parse to a YAML mapping"
    return document


def _condition(config: dict[str, Any]) -> str:
    value = config.get("if")
    return "" if value is None else str(value).strip().lower()


def _continue_on_error_is_disabled(config: dict[str, Any]) -> bool:
    if "continue-on-error" not in config:
        return True
    value = config["continue-on-error"]
    return value is False or (
        isinstance(value, str) and value.strip().lower() == "false"
    )


def test_ci_runs_lint_and_tests_as_executable_fail_closed_steps() -> None:
    workflow = _load_workflow()
    jobs = workflow.get("jobs")
    assert isinstance(jobs, dict) and jobs, "CI must define at least one job"

    observed: dict[str, list[str]] = {"lint": [], "test": []}
    quality_jobs: set[str] = set()
    run_commands: list[str] = []

    for job_name, job in jobs.items():
        assert isinstance(job, dict), f"jobs.{job_name} must be a mapping"
        assert _continue_on_error_is_disabled(job), (
            f"jobs.{job_name} must not suppress job failures"
        )
        steps = job.get("steps") or []
        assert isinstance(steps, list), f"jobs.{job_name}.steps must be a list"

        for index, step in enumerate(steps):
            if not isinstance(step, dict):
                continue
            assert _continue_on_error_is_disabled(step), (
                f"jobs.{job_name}.steps[{index}] must not suppress failures"
            )
            run = step.get("run")
            if not isinstance(run, str):
                continue

            run_commands.append(run)
            assert "||" not in run, (
                f"jobs.{job_name}.steps[{index}] must not mask shell failures"
            )
            command = " ".join(run.split())

            for gate_name, allowed_commands in ALLOWED_QUALITY_COMMANDS.items():
                marker = "ruff check" if gate_name == "lint" else "pytest"
                if marker not in command:
                    continue
                assert command in allowed_commands, (
                    f"{gate_name} must run as a standalone fail-closed command; "
                    f"found {command!r}"
                )
                allowed_conditions = {"", "success()", "${{ success() }}"}
                step_condition = _condition(step)
                job_condition = _condition(job)
                assert step_condition in allowed_conditions, (
                    f"{gate_name} step has a condition that can skip the gate: "
                    f"{step_condition!r}"
                )
                safe_duplicate_run_guard = (
                    job_name == "quality"
                    and job_condition
                    == "github.event_name != 'push' || github.ref == 'refs/heads/main'"
                )
                assert job_condition in allowed_conditions or safe_duplicate_run_guard, (
                    f"job {job_name} has a condition that can skip {gate_name}: "
                    f"{job_condition!r}"
                )
                observed[gate_name].append(job_name)
                quality_jobs.add(job_name)

    for gate_name, job_names in observed.items():
        assert len(job_names) == 1, (
            f"expected exactly one executable {gate_name} command; found {job_names}"
        )

    assert any(
        line.strip() == 'python -m pip install -e ".[dev]"'
        for command in run_commands
        for line in command.splitlines()
    ), "CI must install the project and declared development dependencies"

    # If a separate final gate is introduced, it must depend on every job that
    # performs required lint/test checks.
    gate = jobs.get("gate")
    if isinstance(gate, dict):
        assert _continue_on_error_is_disabled(gate), (
            "the final gate job must not suppress failures"
        )
        gate_condition = _condition(gate)
        assert gate_condition in {"", "success()", "${{ success() }}"}, (
            f"the final gate must not bypass failed quality jobs: {gate_condition!r}"
        )
        needs = gate.get("needs") or []
        if isinstance(needs, str):
            needs = [needs]
        assert isinstance(needs, list), "jobs.gate.needs must be a list or string"
        assert quality_jobs <= set(needs), (
            f"jobs.gate.needs must include all quality jobs: {sorted(quality_jobs)}"
        )

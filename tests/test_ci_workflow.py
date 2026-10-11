from pathlib import Path
import re


def test_ci_workflow_fails_closed_on_lint_and_test_errors() -> None:
    """Require the lint/test steps to run their commands without shell fallbacks."""
    workflow_path = (
        Path(__file__).resolve().parents[1] / ".github" / "workflows" / "ci.yml"
    )
    workflow = workflow_path.read_text(encoding="utf-8")

    # Match the complete run command attached to each named step. Substring-only
    # assertions would miss suppressions such as "ruff check . || :".
    for step_name, expected_command in (
        ("Lint", "ruff check ."),
        ("Test", "pytest -q"),
    ):
        step = re.search(
            rf"(?ms)^\s*- name: {re.escape(step_name)}\s*\n"
            rf"(?P<body>(?:^[ \t]+.*\n)*)",
            workflow,
        )
        assert step is not None, f"missing {step_name} step"
        run_command = re.search(r"(?m)^\s+run:\s*(.*?)\s*$", step.group("body"))
        assert run_command is not None, f"{step_name} step has no run command"
        assert run_command.group(1) == expected_command

    assert "continue-on-error: true" not in workflow

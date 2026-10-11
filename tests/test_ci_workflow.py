"""Regression tests ensuring CI failures cannot be silently ignored."""

from pathlib import Path

WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "ci.yml"


def test_ci_workflow_exists() -> None:
    assert WORKFLOW.is_file(), f"Missing CI workflow: {WORKFLOW}"


def test_ci_does_not_suppress_lint_or_test_failures() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    lowered = workflow.lower()

    forbidden_patterns = (
        "|| true",
        "|| echo",
        "no tests yet",
        "continue-on-error: true",
    )
    for pattern in forbidden_patterns:
        assert pattern not in lowered, (
            f"CI must fail loudly instead of suppressing errors: found {pattern!r}"
        )


def test_ci_runs_lint_and_tests_as_required_steps() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")

    assert "python -m ruff check ." in workflow
    assert "python -m pytest -q" in workflow
    assert 'python -m pip install -e ".[dev]"' in workflow

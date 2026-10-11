from pathlib import Path


def test_ci_workflow_fails_closed_on_lint_and_test_errors() -> None:
    """Guard against CI commands that suppress lint or test failures."""
    workflow_path = (
        Path(__file__).resolve().parents[1] / ".github" / "workflows" / "ci.yml"
    )
    workflow = workflow_path.read_text(encoding="utf-8")

    assert "run: ruff check ." in workflow
    assert "run: pytest -q" in workflow

    # These patterns can turn failed checks into successful workflow steps.
    assert "|| true" not in workflow
    assert "|| echo" not in workflow
    assert "continue-on-error: true" not in workflow

import re
from pathlib import Path


def _workflow() -> str:
    path = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "ci.yml"
    return path.read_text(encoding="utf-8")


def test_ci_workflow_fails_closed_on_lint_and_test_errors() -> None:
    """Require the lint/test steps to run their commands without shell fallbacks."""
    workflow = _workflow()

    for step_name, expected_command in (
        ("Lint", "ruff check ."),
        ("Typecheck", "mypy src tests"),
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
    assert "|| true" not in workflow
    assert "pull_request_target" not in workflow
    assert "persist-credentials: false" in workflow
    assert "contents: read" in workflow

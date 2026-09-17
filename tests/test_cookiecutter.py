"""Tests for the Cookiecutter template."""

from pathlib import Path
from typing import List

from pytest_cookies.plugin import Result


def test_default_project_generation(default_baked_project: Result) -> None:
    """Ensure the template bakes cleanly using default context.

    Args:
        default_baked_project: The result of baking the default template.

    """
    assert default_baked_project.exit_code == 0
    assert default_baked_project.exception is None
    assert default_baked_project.project_path.is_dir()


def test_project_structure(
    default_baked_project: Result, project_dir_structure: List[str]
) -> None:
    """Verify generated project contains the expected files and directories.

    Args:
        default_baked_project: The result of baking the default template.
        project_dir_structure: Expected files and directories in the generated project.

    """
    project_path: Path = default_baked_project.project_path

    missing = [
        item for item in project_dir_structure if not (project_path / item).exists()
    ]

    assert not missing, f"Missing expected files/directories: {missing}"

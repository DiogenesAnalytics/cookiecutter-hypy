"""Tests for the Cookiecutter template."""

from pathlib import Path
from typing import List

import pytest
from pytest_cookies.plugin import Cookies
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


def test_custom_project_generation(cookies: Cookies) -> None:
    """Ensure custom project values are rendered correctly.

    Args:
        cookies: The pytest-cookies fixture.

    """
    result = cookies.bake(
        extra_context={
            "project_name": "my-test-project",
            "package_name": "my_test_project",
            "friendly_name": "My Test Project",
            "description": "A test project.",
            "author": "Test Author",
            "email": "test@example.com",
            "github_user": "TestUser",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert result.project_path.name == "my-test-project"

    package_path = result.project_path / "src" / "my_test_project"

    assert package_path.is_dir()
    assert (package_path / "__init__.py").is_file()
    assert (package_path / "py.typed").is_file()


@pytest.mark.parametrize(
    "license_name,license_exists",
    [
        ("Proprietary", False),
        ("MIT", True),
        ("Apache-2.0", True),
        ("GPL-3.0", True),
    ],
)
def test_license_generation(
    cookies: Cookies, license_name: str, license_exists: bool
) -> None:
    """Verify license selection controls LICENSE generation.

    Args:
        cookies: The pytest-cookies fixture.
        license_name: License selected for the generated project.
        license_exists: Whether LICENSE should be generated.

    """
    result = cookies.bake(
        extra_context={"license": license_name},
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert (result.project_path / "LICENSE").is_file() == license_exists


def test_package_name_transformation(cookies: Cookies) -> None:
    """Verify project names are converted to Python package names.

    Args:
        cookies: The pytest-cookies fixture.

    """
    result = cookies.bake(
        extra_context={
            "project_name": "my-awesome-project",
            "package_name": "my_awesome_project",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None

    package_path = result.project_path / "src" / "my_awesome_project"

    assert package_path.is_dir()
    assert (package_path / "__init__.py").is_file()
    assert (package_path / "py.typed").is_file()


def test_no_unrendered_cookiecutter_variables(
    default_baked_project: Result,
) -> None:
    """Ensure generated files contain no unrendered Cookiecutter variables.

    Args:
        default_baked_project: The generated project.

    """
    project_path: Path = default_baked_project.project_path

    for path in project_path.rglob("*"):
        if not path.is_file():
            continue

        try:
            contents = path.read_text()
        except UnicodeDecodeError:
            continue

        assert "{{ cookiecutter." not in contents, path

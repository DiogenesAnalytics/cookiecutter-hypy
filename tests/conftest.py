"""Pytest configuration and fixtures for testing the Cookiecutter template."""

from typing import List

import pytest
from pytest_cookies.plugin import Cookies
from pytest_cookies.plugin import Result


@pytest.fixture
def default_baked_project(cookies: Cookies) -> Result:
    """Bake the Cookiecutter template using default context.

    Args:
        cookies: The pytest-cookies plugin fixture.

    Returns:
        The result of baking the Cookiecutter template.
    """
    return cookies.bake()


@pytest.fixture
def project_dir_structure() -> List[str]:
    """Return the expected default generated project structure.

    Returns:
        Relative paths expected in the generated project.
    """
    return [
        "Dockerfile",
        "Makefile",
        "notebooks",
        "noxfile.py",
        "poetry.lock",
        "pyproject.toml",
        "README.md",
        "src",
        "src/hypermodern_python",
        "src/hypermodern_python/__init__.py",
        "src/hypermodern_python/py.typed",
        "tests",
        "tests/__init__.py",
        "tests/test_nox.py",
    ]

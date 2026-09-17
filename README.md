
[![tests](https://github.com/DiogenesAnalytics/cookiecutter-hypy/workflows/tests/badge.svg)][tests]
[![Docker](https://github.com/DiogenesAnalytics/cookiecutter-hypy/workflows/docker/badge.svg)][docker]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[tests]: https://github.com/DiogenesAnalytics/cookiecutter-hypy/actions?workflow=tests
[docker]: https://github.com/DiogenesAnalytics/cookiecutter-hypy/actions?workflow=docker
[black]: https://github.com/psf/black

# cookiecutter-hypy

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating modern Python projects following the Diogenes Analytics development conventions.

## Usage

Install Cookiecutter:

```bash
pip install cookiecutter
```

Generate a new project:

```bash
cookiecutter gh:DiogenesAnalytics/cookiecutter-hypy
```

Cookiecutter will prompt for the project name, package name, author information, license, and other project metadata.

## Generated Project

The template provides a ready-to-use Python project with:

* Poetry for dependency management and packaging
* PEP 621 project metadata
* Docker-based development and testing
* pytest for testing
* Black, isort, Flake8, and mypy for code quality
* deptry for dependency checking
* Nox for development automation
* GitHub Actions for continuous integration
* Optional license generation

The generated project uses a `src/` layout and includes the basic infrastructure needed to begin development immediately.

## Development

The template itself is tested by baking a project with Cookiecutter and validating the resulting project structure.

Build the testing image:

```bash
make build-tests
```

Run the test and lint suite:

```bash
make tests
```

Run the available checks:

```bash
make check-all
```

## License

The template is available under the MIT License.

# {{cookiecutter.friendly_name}}

{{cookiecutter.description}}

[![tests](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/tests/badge.svg)][tests]
[![Docker](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/docker/badge.svg)][docker]
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[tests]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=tests
[docker]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=docker
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _{{cookiecutter.friendly_name}}_ as follows:

```console
$ pip install git+https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
```

## License

{% if cookiecutter.license != 'Proprietary' -%}
Distributed under the terms of the [{{cookiecutter.license.replace("-", " ")}} license][license],
_{{cookiecutter.friendly_name}}_ is free and open source software.
{%- else -%}
Proprietary
{%- endif %}

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python

{% if cookiecutter.license != 'Proprietary' -%}
<!-- github-only -->
[license]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/LICENSE
{%- else -%}
<!-- github-only -->
{%- endif %}

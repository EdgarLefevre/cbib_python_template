# {{ cookiecutter.project_name }}

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_username  }}/{{ cookiecutter.project_slug }}?label=license)](https://github.com/EdgarLefevre/{{ cookiecutter.project_slug }}/blob/main/LICENSE)
{% if cookiecutter.tests == "y" %}
[![tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Tests/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg?token=H41ZaCAg31)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% endif %}

![CBiB Logo](imgs/cbib_logo.png)

----------------------------
## things to do
- go to settings-> action -> enable repo modification
{% if cookiecutter.tests == "y" %}
- if the repo of private: add codecov secret "CODECOV_TOKEN", go to codecov website, enable repo, copy token and on github go to settings, add secret
{% endif %}
------------------------------
## Installation
To use this project, we advise you to create a fresh virtual environment.

We use conda: 
```shell
conda env create -f environment.yml
```

But if you do not have conda, you can use pip:
```shell
pip install -r requirements.txt
```

>**Note**: requirements.txt is necessary for github actions. DO NOT REMOVE IT.

## Run code
To run the code, go to the project's root directory and run:
```shell
python -m {{ cookiecutter.src_dir}}.{{ cookiecutter.main_file}}
```
{% if cookiecutter.docs == "y" %}
## Generate documentation

The documentation is handeled by [Sphinx](https://www.sphinx-doc.org/en/master/)
To generate the documentation, run the following commands:
```shell
cd docs
make html
```

The folder is already configured with autodoc and read the doc theme
{% endif %}
{% if cookiecutter.tests == "y" %}

## Run tests 

Test are handeled by [Pytest](https://docs.pytest.org/en/latest/getting-started.html).

To run the tests, run the following commands:

```shell
python -m pytest  # assuming you are at the project root
```
{% endif %}

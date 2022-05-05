import os
import sys
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.tests != "y" %} tests/ {% endif %}',
    '{% if cookiecutter.docs != "y" %} docs/ {% endif %}',
    '{% if cookiecutter.github_actions != "y" %} .github/ {% endif %}',
    '{% if cookiecutter.notebooks != "y" %} notebooks/ {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
           shutil .rmtree(path, ignore_errors=True)
        else:
            os.unlink(path)

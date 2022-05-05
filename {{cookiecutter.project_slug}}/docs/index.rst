{% set file_name = cookiecutter.main_file.split('.')[0] %}
Welcome to {{cookiecutter.project_name}}'s documentation!
=========================================================
.. automodule:: {{cookiecutter.src_dir}}.{{ file_name }}
    :members:
    :members-order: bysource

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

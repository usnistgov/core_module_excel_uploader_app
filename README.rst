core_module_excel_uploader_app
==============================

Excel Uploader module for the parser core project. A sample file is provided in the static folder.

Quick start
===========

1. Add "core_module_excel_uploader_app" to your INSTALLED_APPS setting
----------------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_module_excel_uploader_app',
    ]

2. Include the core_module_excel_uploader_app URLconf in your project urls.py
-----------------------------------------------------------------------------

.. code:: python

    url(r'^', include('core_module_excel_uploader_app.urls')),
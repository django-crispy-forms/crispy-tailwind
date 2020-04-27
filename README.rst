===============
Crispy-Tailwind
===============

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


A Tailwind_ template pack for the wonderful django-crispy-forms_.

How to install
--------------

Install via PIP::

    pip install crispy-tailwind

You will need to update your project's settings file to add  crispy_forms
and crispy_tailwind to your projects `INSTALLED_APPS`, and to set `tailwind`
as the default template pack for your project::

    INSTALLED_APPS = (
        ...
        'crispy_forms',
        'crispy_forms_materialize',
        ...
    )

    # Default template pack to use with "crispy_forms"
    CRISPY_TEMPLATE_PACK = 'materialize_css_forms'


How to use
----------

TODO



.. _tailwind: https://tailwindcss.com/
.. _django-crispy-forms: https://github.com/django-crispy-forms/django-crispy-forms

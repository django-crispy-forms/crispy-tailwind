===============
Crispy-Tailwind
===============

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

A Tailwind_ template pack for the wonderful django-crispy-forms_.

**WARNING**

This project is still in its early stages of development. Any contributions to
the package would be very welcomed.

Currently the template pack allows the use of the ``|crispy`` filter to style
your form. Here is an example image.

.. image:: https://django-crispy-forms.github.io/crispy-tailwind/_images/crispy_form.png

How to install
--------------

Install via pip. ::

    pip install crispy-tailwind

You will need to update your project's settings file to add ``crispy_forms``
and ``crispy_tailwind`` to your projects ``INSTALLED_APPS``. Also set
``tailwind`` as and allowed template pack and as the default template pack
for your project::

    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_tailwind",
        ...
    )

    CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

    CRISPY_TEMPLATE_PACK = "tailwind"

How to use
----------

This project is still in its early stages.

Currently functionality allows the ``|crispy`` filter to be used to style your
form. In your template:

1. Load the filter ``{% load tailwind_filters %}``
2. Apply the crispy filter ``{{ form|crispy }}``

We can also use the ``{% crispy %}`` tag to allow usage of crispy-forms'
``FormHelpler`` and ``Layout``. In your template:

1. Load the crispy tag ``{% load crispy_forms_tags %}``
2. Add ``FormHelper`` to your form and use crispy-forms to set-up your form
2. Use the crispy tag ``{% crispy form %}`` in your template.

Documentation
-------------

The documentation for this project is available here:
https://django-crispy-forms.github.io/crispy-tailwind/index.html







.. _tailwind: https://tailwindcss.com/
.. _django-crispy-forms: https://github.com/django-crispy-forms/django-crispy-forms

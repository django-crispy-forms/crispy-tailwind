CHANGELOG
=========

1.0.3 - 2024-02-13
------------------

* Fixed stray closing divs in template files (second try 😅)

Contributed by [Ronny V.](https://github.com/GitRon) via [PR #162](https://github.com/django-crispy-forms/crispy-tailwind/pull/162/)


1.0.2 - 2024-02-13
------------------

* Fixed stray closing divs in template files

Contributed by [Ronny V.](https://github.com/GitRon) via [PR #160](https://github.com/django-crispy-forms/crispy-tailwind/pull/160/)


1.0.1 - 2024-02-06
------------------

* Add `build_attrs` filter to `tailwind_filters.py`
* Add `attrs.html` template for Tailwind layout
* Refactor `select.html` and `select_option.html` templates
* Add ID attribute to `select` elements

1.0.0 - 2024-01-09
------------------

* Added support for Django 5.0 (#142)
* Added support for Python 3.11 and 3.12 (#142)
* Added support for Python 3.10 (#116)
* Added support for Django 4.2 (#135)
* Dropped support for Django 2.2 (#116)
* Dropped support for Django 3.2, 4.0 and 4.1 (#138)
* Dropped support for Python 3.6 (#116)
* Dropped support for Python 3.7 (#135)
* Increased minimum supported django-crispy-forms version to 2.0 (#135)
* Added docs about Tailwind CLI template discovery management command (#144)
* Fixed bug with select template and disabled property (#118)

0.5.0 - 2021-04-21
------------------

* Added support for custom widgets (#92)
* Confirmed support for Django 3.2 (#91)
* Dropped support for Django 3.1 (#91)

See [Release Notes](https://github.com/django-crispy-forms/crispy-tailwind/milestone/5?closed=1)
for full change log.

0.4.0 - 2021-03-22
------------------

* Fixed compatibility with django-crispy-forms 1.11.2 (#86)
* Fixed field names when using formsets (#84)

See [Release Notes](https://github.com/django-crispy-forms/crispy-tailwind/milestone/4?closed=1)
for full change log.

0.3.0 - 2021-02-14
------------------

* Fixed non form errors (#77)
* Various documentation improvements
* Python 3.9 (#60) and Django 3.1 (#56) support

See [Release Notes](https://github.com/django-crispy-forms/crispy-tailwind/milestone/3?closed=1)
for full change log.

0.2.0 - 2020-07-11
------------------

* Support for Formsets
* Prepended and Appended inputs
* Customisable buttons
* Much improved test coverage
* Improved documentation. Docs now include details on how to use the majority
  of the core layout objects, crispy filter and add-on

See [Release Notes](https://github.com/django-crispy-forms/crispy-tailwind/milestone/2?closed=1)
for full change log.

0.1.0 - 2020-06-09
------------------

* First Release, please do come and test!
* Opinionated forms can be rendered with crispy filter
* Limited set of layout objects are also available for crispy tags, also with
  opinionated rendering.

See [Release Notes](https://github.com/django-crispy-forms/crispy-tailwind/milestone/1)
for full change log

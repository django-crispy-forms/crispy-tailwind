import django
from django.forms.models import formset_factory
from django.template import Context, Template
from django.test import SimpleTestCase
from django.test.html import parse_html

from .forms import CharFieldForm, SampleForm, ShortCharFieldForm
from .utils import parse_expected


class CrispyFilterTests(SimpleTestCase):
    maxDiff = None

    def test_crispy_filter(self):
        template = Template(
            """
            {% load tailwind_filters %}
            {{ form|crispy }}
            """
        )
        form = SampleForm()
        c = Context({"form": form})
        html = template.render(c)
        if django.VERSION < (5, 0):
            expected = "filter/crispy_filter_lt50.html"
        else:
            expected = "filter/crispy_filter.html"
        assert parse_html(html) == parse_expected(expected)

    def test_error_borders(self):
        template = Template(
            """
            {% load tailwind_filters %}
            {{ form|crispy }}
            """
        )
        form = CharFieldForm()
        c = Context({"form": form})
        html = template.render(c)
        assert "border-red-500" not in html
        assert "border-gray-300" in html

        form = CharFieldForm({"name": ""})
        c = Context({"form": form})
        html = template.render(c)
        assert "border-red-500" in html
        assert "border-gray-300" not in html

    def test_formset(self):
        template = Template(
            """
            {% load tailwind_filters %}
            {{ form|crispy }}
            """
        )
        formset = formset_factory(ShortCharFieldForm, extra=2)
        c = Context({"form": formset})
        html = template.render(c)
        assert parse_html(html) == parse_expected("filter/formset.html")

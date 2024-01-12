from django.template import Context, Template
from django.test import SimpleTestCase
from django.test.html import parse_html

from .forms import SampleForm
from .utils import parse_expected


class CrispyHelperTests(SimpleTestCase):
    maxDiff = None

    def test_crispy_addon(self):
        template = Template(
            """
            {% load tailwind_field %}
            {% crispy_addon form.last_name prepend="$" append=".00" %}
            """
        )
        html = template.render(Context({"form": SampleForm()}))
        assert parse_html(html) == parse_expected("crispy_addon/crispy_addon.html")

from django.template import Template
from django.test import SimpleTestCase

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_tailwind.layout import Alert

from .forms import SampleForm
from .utils import parse_expected, parse_form

template = Template(
    """
    {% load crispy_forms_tags %}
    {% crispy form %}
    """
)


class CrispyHelperTests(SimpleTestCase):
    maxDiff = None

    def test_alert(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(Alert(content="<strong>Warning!</strong> Here's a test message."))
        assert parse_form(form) == parse_expected("alert/alert.html")

    def test_dismiss_false(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(Alert(dismiss=False, content="<strong>Warning!</strong> Here's a test message."))
        assert parse_form(form) == parse_expected("alert/alert_dismiss_false.html")

    def test_custom_alert(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            Alert(content="<strong>Warning!</strong> Here's a test message.", css_class="custom css")
        )
        assert parse_form(form) == parse_expected("alert/alert_custom.html")

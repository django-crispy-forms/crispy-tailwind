from django.template import Template
from django.test import SimpleTestCase

from crispy_forms.bootstrap import AppendedText, PrependedAppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from .forms import CharFieldForm, SampleForm
from .utils import parse_expected, parse_form

template = Template(
    """
    {% load crispy_forms_tags %}
    {% crispy form %}
    """
)


class CrispyHelperTests(SimpleTestCase):
    maxDiff = None

    def test_prepended_text(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(PrependedText("first_name", "@"))
        assert parse_form(form) == parse_expected("prepended/prepended_text.html")

    def test_prepended_long_text(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(PrependedText("first_name", "http://www."))
        assert parse_form(form) == parse_expected("prepended/prepended_long_text.html")

    def test_appended_text(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(AppendedText("first_name", ".com"))
        assert parse_form(form) == parse_expected("prepended/appended_text.html")

    def test_prepended_and_appended_text(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(PrependedAppendedText("first_name", "www.", ".com"))
        assert parse_form(form) == parse_expected("prepended/prepended_appended_text.html")

    def test_prepended_text_no_label(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedText("first_name", "@"))
        assert parse_form(form) == parse_expected("prepended/prepended_no_label.html")

    def test_prepended_with_help(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedText("email", "@"))
        assert parse_form(form) == parse_expected("prepended/prepended_help.html")

    def test_prepended_with_errors(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedText("name", "@"))
        assert parse_form(form) == parse_expected("prepended/prepended_errors.html")

    def test_appended_with_errors(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(AppendedText("name", "@"))
        assert parse_form(form) == parse_expected("prepended/appended_errors.html")

    def test_prepended_and_appended_with_errors(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedAppendedText("name", "@", ".com"))
        assert parse_form(form) == parse_expected("prepended/prepended_appended_errors.html")

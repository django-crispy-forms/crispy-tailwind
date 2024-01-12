import django
from django.forms.models import formset_factory
from django.template import Template
from django.test import SimpleTestCase

from crispy_forms.bootstrap import FieldWithButtons, InlineCheckboxes, InlineField, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Div, Field, Fieldset, Hidden, Layout, Row
from crispy_forms.utils import render_crispy_form
from crispy_tailwind.layout import Button, Reset, Submit

from .forms import (
    CharFieldForm,
    CheckboxMultiple,
    PasswordFieldForm,
    RadioForm,
    SampleForm,
    SelectForm,
    ShortCharFieldForm,
)
from .utils import parse_expected, parse_form

template = Template(
    """
    {% load crispy_forms_tags %}
    {% crispy form %}
    """
)


class CrispyHelperTests(SimpleTestCase):
    maxDiff = None

    def test_CharField(self):
        form = CharFieldForm()
        form.helper = FormHelper()
        assert parse_form(form) == parse_expected("helper/charfield.html")

    def test_failing_CharField(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        if django.VERSION < (5, 0):
            expected = "helper/charfield_failing_lt50.html"
        else:
            expected = "helper/charfield_failing.html"
        assert parse_form(form) == parse_expected(expected)

    def test_password(self):
        form = PasswordFieldForm()
        form.helper = FormHelper()
        assert parse_form(form) == parse_expected("helper/password.html")

    def test_radio(self):
        form = RadioForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        assert parse_form(form) == parse_expected("helper/radio.html")

    def test_multiple_checkbox(self):
        form = CheckboxMultiple()
        form.helper = FormHelper()
        form.helper.form_tag = False
        assert parse_form(form) == parse_expected("helper/multiple_checkbox.html")

    def test_crispy_layout(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.layout = Layout("is_company", "first_name")
        form.helper.form_tag = False
        assert parse_form(form) == parse_expected("helper/crispy_layout.html")

    def test_col_row(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            Row(
                Column(Field("first_name"), Field("last_name"), css_class="px-2"),
                Column("email", css_class="px-2"),
            )
        )
        if django.VERSION < (5, 0):
            expected = "helper/col_row_lt50.html"
        else:
            expected = "helper/col_row.html"
        assert parse_form(form) == parse_expected(expected)

    def test_inline_radio(self):
        form = RadioForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(InlineRadios("radio"))
        assert parse_form(form) == parse_expected("helper/inline_radio.html")

    def test_inline_checkbox(self):
        form = CheckboxMultiple()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(InlineCheckboxes("checkbox"))
        assert parse_form(form) == parse_expected("helper/inline_checkbox.html")

    def test_formset(self):
        SampleFormSet = formset_factory(SampleForm, extra=2)
        formset = SampleFormSet()
        formset.helper = FormHelper()
        formset.helper.form_tag = False
        formset.helper.layout = Layout("email")
        if django.VERSION < (5, 0):
            expected = "helper/formset_lt50.html"
        else:
            expected = "helper/formset.html"
        assert parse_form(formset) == parse_expected(expected)

    def test_formset_with_errors(self):
        SampleFormSet = formset_factory(ShortCharFieldForm, extra=1, max_num=2, validate_max=True)
        data = {
            "name-0-name": "test",
            "name-INITIAL_FORMS": "0",
            "name-MIN_NUM_FORMS": "0",
            "name-MAX_NUM_FORMS": "0",
            "name-TOTAL_FORMS": "3",
        }
        formset = SampleFormSet(data=data, prefix="name")
        formset.helper = FormHelper()
        formset.helper.formset_error_title = "Non Form Errors"
        formset.helper.form_tag = False
        formset.helper.layout = Layout("email")
        if django.VERSION < (5, 0):
            expected = "helper/formset_errors_lt50.html"
        else:
            expected = "helper/formset_errors.html"
        assert parse_form(formset) == parse_expected(expected)

    def test_formset_with_form_tag(self):
        SampleFormSet = formset_factory(SampleForm, extra=2)
        formset = SampleFormSet()
        formset.helper = FormHelper()
        formset.helper.form_tag = True
        formset.helper.layout = Layout("email")
        if django.VERSION < (5, 0):
            expected = "helper/formset_form_tag_lt50.html"
        else:
            expected = "helper/formset_form_tag.html"
        assert parse_form(formset) == parse_expected(expected)

    def test_buttons(self):
        form = CharFieldForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            Button("button", "Button"),
            Submit(
                "submit",
                "Submit",
            ),
            Reset("cancel", "Cancel"),
        )
        assert parse_form(form) == parse_expected("helper/buttons.html")

        form.helper.layout = Layout(
            Submit(
                "submit",
                "Submit",
                css_class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded",
            )
        )
        assert parse_form(form) == parse_expected("helper/buttons_with_css.html")

    def test_div(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(Div("email", "name", css_class="test class"))
        if django.VERSION < (5, 0):
            expected = "helper/div_lt50.html"
        else:
            expected = "helper/div.html"
        assert parse_form(form) == parse_expected(expected)

    def test_HTML(self):
        form = CharFieldForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(HTML('<span class="mb-2">Test HTML Layout</span>'))
        html = render_crispy_form(form)
        expected_html = '<span class="mb-2">Test HTML Layout</span>'
        self.assertHTMLEqual(html, expected_html)

    def test_hidden(self):
        form = CharFieldForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(Hidden("name", "value"))
        html = render_crispy_form(form)
        expected_html = '<input type="hidden" name="name" value="value"/>'
        self.assertHTMLEqual(html, expected_html)

    def test_fieldset(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            Fieldset(
                "Text for the legend",
                "is_company",
                "email",
            )
        )
        if django.VERSION < (5, 0):
            expected = "helper/fieldset_lt50.html"
        else:
            expected = "helper/fieldset.html"
        assert parse_form(form) == parse_expected(expected)

    def test_non_form_errors(self):
        form = SampleForm(data={})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_error_title = "Form Error Title"
        form.helper.layout = Layout("password1", "password2")
        if django.VERSION < (5, 0):
            expected = "helper/non_form_errors_lt50.html"
        else:
            expected = "helper/non_form_errors.html"
        assert parse_form(form) == parse_expected(expected)

    def test_select(self):
        form = SelectForm(data={"tos_accepted": "accepted"})
        form.helper = FormHelper()
        form.helper.form_tag = False
        parse_form(form) == parse_expected("helper/select.html")

    def test_field_with_buttons(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            FieldWithButtons("first_name", Button("Go!", "go")),
        )
        assert parse_form(form) == parse_expected("helper/field_with_buttons.html")

    def test_inline_field(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            InlineField("first_name"),
            InlineField("is_company"),
        )
        assert parse_form(form) == parse_expected("helper/inline_field.html")

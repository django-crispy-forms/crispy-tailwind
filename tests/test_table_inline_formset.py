import django
from django.forms import formset_factory
from django.test import SimpleTestCase

from crispy_forms.helper import FormHelper
from crispy_tailwind.layout import Submit

from .forms import SampleForm, ShortCharFieldForm
from .utils import parse_expected, parse_form


class CrispyHelperTests(SimpleTestCase):
    maxDiff = None

    def test_table_inline_formset(self):
        SampleFormSet = formset_factory(SampleForm, extra=2)
        formset = SampleFormSet()
        formset.helper = FormHelper()
        formset.helper.form_tag = False
        formset.helper.add_input(Submit("submit", "submit"))
        formset.helper.template = "tailwind/table_inline_formset.html"
        if django.VERSION < (5, 0):
            expected = "table_inline_formset/table_inline_formset_lt50.html"
        else:
            expected = "table_inline_formset/table_inline_formset.html"
        assert parse_form(formset) == parse_expected(expected)

    def test_failing_table_inline_formset(self):
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
        formset.helper.add_input(Submit("submit", "submit"))
        formset.helper.template = "tailwind/table_inline_formset.html"
        if django.VERSION < (5, 0):
            expected = "table_inline_formset/table_inline_formset_failing_lt50.html"
        else:
            expected = "table_inline_formset/table_inline_formset_failing.html"
        assert parse_form(formset) == parse_expected(expected)

from django.template import Template
from django.test import SimpleTestCase

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.utils import render_crispy_form
from crispy_tailwind.layout import Alert

from .forms import SampleForm

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
        html = render_crispy_form(form)
        expected_html = """
          <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <div class="block sm:inline"><strong>Warning!</strong> Here's a test message.</div>
            <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
                <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                    <title>Close</title>
                    <path
                        d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"
                    />
                </svg>
            </span>
        </div>
        """
        self.assertHTMLEqual(html, expected_html)

    def test_dismiss_false(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(Alert(dismiss=False, content="<strong>Warning!</strong> Here's a test message."))
        html = render_crispy_form(form)
        expected_html = """
          <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <div class="block sm:inline"><strong>Warning!</strong> Here's a test message.</div>
        </div>
        """
        self.assertHTMLEqual(html, expected_html)

    def test_custom_alert(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            Alert(content="<strong>Warning!</strong> Here's a test message.", css_class="custom css")
        )
        html = render_crispy_form(form)
        expected_html = """
            <div class=" custom css" role="alert">
                <div class="block sm:inline"><strong>Warning!</strong> Here's a test message.</div>
                <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
                    <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <title>Close</title>
                        <path
                            d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"
                        />
                    </svg>
                </span>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

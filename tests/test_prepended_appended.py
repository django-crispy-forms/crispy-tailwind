from django.template import Template
from django.test import SimpleTestCase

from crispy_forms.bootstrap import AppendedText, PrependedAppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.utils import render_crispy_form

from .forms import CharFieldForm, SampleForm

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
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_first_name" class="mb-3">
                <label for="id_first_name" class="block text-gray-700 text-sm font-bold mb-2"> first name<span class="asteriskField">*</span> </label>
                <div class="">
                    <div class="flex">
                        <span class="border rounded-lg border-gray-300 rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">@</span>
                        <input
                            type="text"
                            name="first_name"
                            maxlength="5"
                            class="textinput textInput inputtext border border-gray-300 rounded-lg rounded-l-none px-4 py-2 w-full focus:outline-none text-gray-700 border-l-0 leading-normal"
                            required
                            id="id_first_name"
                        />
                    </div>
                </div>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_prepended_long_text(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(PrependedText("first_name", "http://www."))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_first_name" class="mb-3">
                <label for="id_first_name" class="block text-gray-700 text-sm font-bold mb-2"> first name<span class="asteriskField">*</span> </label>
                <div class="">
                    <div class="flex">
                        <span class="border rounded-lg border-gray-300 rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">http://www.</span>
                        <input
                            type="text"
                            name="first_name"
                            maxlength="5"
                            class="textinput textInput inputtext border border-gray-300 rounded-lg rounded-l-none px-4 py-2 w-full focus:outline-none text-gray-700 border-l-0 leading-normal"
                            required
                            id="id_first_name"
                        />
                    </div>
                </div>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_appended_text(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(AppendedText("first_name", ".com"))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_first_name" class="mb-3">
                <label for="id_first_name" class="block text-gray-700 text-sm font-bold mb-2"> first name<span class="asteriskField">*</span> </label>
                <div class="">
                    <div class="flex">
                        <input
                            type="text"
                            name="first_name"
                            maxlength="5"
                            class="textinput textInput inputtext border border-gray-300 rounded-lg rounded-r-none px-4 py-2 w-full focus:outline-none text-gray-700 border-r-0 leading-normal"
                            required
                            id="id_first_name"
                        />
                        <span class="border rounded-lg border-gray-300 rounded-l-none px-3 bg-gray-200 text-gray-800 flex items-center">.com</span>
                    </div>
                </div>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_prepended_and_appended_text(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(PrependedAppendedText("first_name", "www.", ".com"))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_first_name" class="mb-3">
                <label for="id_first_name" class="block text-gray-700 text-sm font-bold mb-2"> first name<span class="asteriskField">*</span> </label>
                <div class="">
                    <div class="flex">
                        <span class="border rounded-lg border-gray-300 rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">www.</span>
                        <input type="text" name="first_name" maxlength="5" class="textinput textInput inputtext border border-gray-300 px-4 py-2 w-full focus:outline-none text-gray-700 border-r-0 leading-normal" required id="id_first_name" />
                        <span class="border rounded-lg border-gray-300 rounded-l-none px-3 bg-gray-200 text-gray-800 flex items-center">.com</span>
                    </div>
                </div>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_prepended_text_no_label(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedText("first_name", "@"))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_first_name" class="mb-3">
                <div class="">
                    <div class="flex">
                        <span class="border rounded-lg border-gray-300 rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">@</span>
                        <input
                            type="text"
                            name="first_name"
                            maxlength="5"
                            class="textinput textInput inputtext border border-gray-300 rounded-lg rounded-l-none px-4 py-2 w-full focus:outline-none text-gray-700 border-l-0 leading-normal"
                            required
                            id="id_first_name"
                        />
                    </div>
                </div>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_prepended_with_help(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedText("email", "@"))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_email" class="mb-3">
                <div class="">
                    <div class="flex">
                        <span class="border rounded-lg border-gray-300 rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">@</span>
                        <input
                            type="text"
                            name="email"
                            maxlength="30"
                            class="textinput textInput inputtext border border-gray-300 rounded-lg rounded-l-none px-4 py-2 w-full focus:outline-none text-gray-700 border-l-0 leading-normal"
                            required
                            id="id_email"
                        />
                    </div>
                </div>
                <small id="hint_id_email" class="text-gray-600">Insert your email</small>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_prepended_with_errors(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedText("name", "@"))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_name" class="mb-3">
                <div class="">
                    <div class="flex">
                        <span class="border-red-500 border-r-0 border rounded-lg rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">@</span>
                        <input type="text" name="name" class="textinput textInput inputtext border border-red-500 rounded-lg rounded-l-none px-4 py-2 w-full focus:outline-none text-gray-700 border-l-0 leading-normal" required id="id_name" />
                    </div>
                </div>
                <p id="error_1_id_name" class="text-red-500 text-xs italic"><strong>This field is required.</strong></p>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_appended_with_errors(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(AppendedText("name", "@"))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_name" class="mb-3">
                <div class="">
                    <div class="flex">
                        <input type="text" name="name" class="textinput textInput inputtext border border-red-500 rounded-lg rounded-r-none px-4 py-2 w-full focus:outline-none text-gray-700 border-r-0 leading-normal" required id="id_name" />
                        <span class="border-red-500 border-l-0 border rounded-lg rounded-l-none px-3 bg-gray-200 text-gray-800 flex items-center">@</span>
                    </div>
                </div>
                <p id="error_1_id_name" class="text-red-500 text-xs italic"><strong>This field is required.</strong></p>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_prepended_and_appended_with_errors(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_show_labels = False
        form.helper.layout = Layout(PrependedAppendedText("name", "@", ".com"))
        html = render_crispy_form(form)
        expected_html = """
            <div id="div_id_name" class="mb-3">
                <div class="">
                    <div class="flex">
                        <span class="border-red-500 border-r-0 border rounded-lg rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">@</span>
                        <input type="text" name="name" class="textinput textInput inputtext border border-r-0 border-l-0 border-red-500 px-4 py-2 w-full focus:outline-none text-gray-700 border-r-0 leading-normal" required id="id_name" />
                        <span class="border-red-500 border-l-0 border rounded-lg rounded-l-none px-3 bg-gray-200 text-gray-800 flex items-center">.com</span>
                    </div>
                </div>
                <p id="error_1_id_name" class="text-red-500 text-xs italic"><strong>This field is required.</strong></p>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

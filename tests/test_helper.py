from django.forms.models import formset_factory
from django.template import Context, Template
from django.test import SimpleTestCase

from crispy_forms.bootstrap import InlineCheckboxes, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row
from crispy_forms.utils import render_crispy_form
from crispy_tailwind.layout import Button, Reset, Submit

from .forms import CharFieldForm, CheckboxMultiple, PasswordFieldForm, RadioForm, SampleForm

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
        html = render_crispy_form(form)
        expected_html = """
            <form method="post">
                <div id="div_id_name" class="mb-3">
                    <label for="id_name" class="block font-bold mb-2 text-gray-700 text-sm"> Name<span class="asteriskField">*</span> </label>
                    <input type="text" name="name" class="textinput textInput inputtext block bg-white rounded-lg leading-normal border-gray-300 px-4 appearance-none border focus:outline-none w-full py-2 text-gray-700" required id="id_name" />
                </div>
            </form>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_password(self):
        form = PasswordFieldForm()
        form.helper = FormHelper()
        html = render_crispy_form(form)
        expected_html = """
            <form method="post">
                <div id="div_id_password" class="mb-3">
                    <label for="id_password" class="block font-bold mb-2 text-gray-700 text-sm"> Password<span class="asteriskField">*</span> </label>
                    <input type="password" name="password" class="passwordinput bg-white text-gray-700 w-full px-4 border py-2 border-gray-300 block rounded-lg focus:outline-none leading-normal appearance-none" required id="id_password" />
                </div>
            </form>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_radio(self):
        form = RadioForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        html = render_crispy_form(form)
        expected_html = """
                <div id="div_id_radio" class="mb-3">
                    <label for="id_radio_0" class="block font-bold mb-2 text-gray-700 text-sm"> Radio<span class="asteriskField">*</span> </label>
                    <div class="mb-3">
                        <label for="id_radio_1" class="block text-gray-700 mr-3">
                            <input type="radio" class="" name="radio" id="id_radio_1" value="blue" />
                            Blue
                        </label>
                        <label for="id_radio_2" class="block text-gray-700 mr-3">
                            <input type="radio" class="" name="radio" id="id_radio_2" value="green" />
                            Green
                        </label>
                    </div>
                </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_multiple_checkbox(self):
        form = CheckboxMultiple()
        form.helper = FormHelper()
        form.helper.form_tag = False
        html = render_crispy_form(form)
        expected_html = """
                <div id="div_id_checkbox" class="mb-3">
                    <label for="" class="block font-bold mb-2 text-gray-700 text-sm"> Checkbox<span class="asteriskField">*</span> </label>
                    <div class="mb-3">
                        <div class="mr-3">
                            <label class="block text-gray-700" for="id_checkbox_1">
                                <input type="checkbox" class="" name="checkbox" id="id_checkbox_1" value="blue" />
                                Blue
                            </label>
                        </div>
                        <div class="mr-3">
                            <label class="block text-gray-700" for="id_checkbox_2">
                                <input type="checkbox" class="" name="checkbox" id="id_checkbox_2" value="green" />
                                Green
                            </label>
                        </div>
                    </div>
                </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_crispy_layout(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.layout = Layout("is_company", "first_name")
        form.helper.form_tag = False
        html = render_crispy_form(form)
        expected_html = """
                <div id="div_id_is_company" class="mb-3">
                    <label for="id_is_company" class="block font-bold mb-2 text-gray-700 text-sm">
                        company
                    </label>
                    <input type="checkbox" name="is_company" class=" checkboxinput" id="id_is_company" />
                </div>
                <div id="div_id_first_name" class="mb-3">
                    <label for="id_first_name" class="block font-bold mb-2 text-gray-700 text-sm"> first name<span class="asteriskField">*</span> </label>
                    <input
                        type="text"
                        name="first_name"
                        maxlength="5"
                        class="textinput textInput inputtext rounded-lg leading-normal border text-gray-700 w-full block border-gray-300 appearance-none bg-white focus:outline-none px-4 py-2"
                        required
                        id="id_first_name"
                    />
                </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_col_row(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(
            Row(Column(Field("first_name"), Field("last_name"), css_class="px-2"), Column("email", css_class="px-2"),)
        )
        html = render_crispy_form(form)
        expected_html = """
            <div class="flex flex-row">
                <div class="px-2">
                    <div id="div_id_first_name" class="mb-3">
                        <label for="id_first_name" class="block text-gray-700 text-sm font-bold mb-2"> first name<span class="asteriskField">*</span> </label>
                        <input
                            type="text"
                            name="first_name"
                            maxlength="5"
                            class="textinput textInput inputtext border w-full bg-white appearance-none block focus:outline-none leading-normal py-2 border-gray-300 text-gray-700 rounded-lg px-4"
                            required
                            id="id_first_name"
                        />
                    </div>
                    <div id="div_id_last_name" class="mb-3">
                        <label for="id_last_name" class="block text-gray-700 text-sm font-bold mb-2"> last name<span class="asteriskField">*</span> </label>
                        <input
                            type="text"
                            name="last_name"
                            maxlength="5"
                            class="textinput textInput inputtext border w-full bg-white appearance-none block focus:outline-none leading-normal py-2 border-gray-300 text-gray-700 rounded-lg px-4"
                            required
                            id="id_last_name"
                        />
                    </div>
                </div>
                <div class="px-2">
                    <div id="div_id_email" class="mb-3">
                        <label for="id_email" class="block text-gray-700 text-sm font-bold mb-2"> email<span class="asteriskField">*</span> </label>
                        <input
                            type="text"
                            name="email"
                            maxlength="30"
                            class="textinput textInput inputtext border w-full bg-white appearance-none block focus:outline-none leading-normal py-2 border-gray-300 text-gray-700 rounded-lg px-4"
                            required
                            id="id_email"
                        />
                        <small id="hint_id_email" class="text-gray-600">Insert your email</small>
                    </div>
                </div>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_inline_radio(self):
        form = RadioForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(InlineRadios("radio"))
        html = render_crispy_form(form)
        expected_html = """
                <div id="div_id_radio" class="mb-3">
                    <label for="id_radio_0" class=" block text-gray-700 text-sm font-bold mb-2 requiredField"> Radio<span class="asteriskField">*</span> </label>
                    <div id="div_id_radio" class="flex flex-row">
                        <label for="id_radio_1" class="block text-gray-700 mr-3">
                            <input type="radio" class="" name="radio" id="id_radio_1" value="blue" />
                            Blue
                        </label>
                        <label for="id_radio_2" class="block text-gray-700 mr-3">
                            <input type="radio" class="" name="radio" id="id_radio_2" value="green" />
                            Green
                        </label>
                    </div>
                </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_inline_checkbox(self):
        form = CheckboxMultiple()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(InlineCheckboxes("checkbox"))
        html = render_crispy_form(form)
        expected_html = """
                <div id="div_id_checkbox" class="mb-3">
                    <label for="" class="block text-gray-700 text-sm font-bold mb-2 requiredField"> Checkbox<span class="asteriskField">*</span> </label>
                    <div id="div_id_checkbox" class="flex flex-row">
                        <div class="mr-3">
                            <label class="block text-gray-700" for="id_checkbox_1">
                                <input type="checkbox" class="" name="checkbox" id="id_checkbox_1" value="blue" />
                                Blue
                            </label>
                        </div>
                        <div class="mr-3">
                            <label class="block text-gray-700" for="id_checkbox_2">
                                <input type="checkbox" class="" name="checkbox" id="id_checkbox_2" value="green" />
                                Green
                            </label>
                        </div>
                    </div>
                </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_formset(self):
        SampleFormSet = formset_factory(SampleForm, extra=2)
        formset = SampleFormSet()
        formset.helper = FormHelper()
        formset.helper.form_tag = False
        formset.helper.layout = Layout("email")
        html = render_crispy_form(formset)
        expected_html = """
            <div>
                <input type="hidden" name="form-TOTAL_FORMS" value="2" id="id_form-TOTAL_FORMS" /> <input type="hidden" name="form-INITIAL_FORMS" value="0" id="id_form-INITIAL_FORMS" />
                <input type="hidden" name="form-MIN_NUM_FORMS" value="0" id="id_form-MIN_NUM_FORMS" /> <input type="hidden" name="form-MAX_NUM_FORMS" value="1000" id="id_form-MAX_NUM_FORMS" />
            </div>
            <div id="div_id_form-0-email" class="mb-3">
                <label for="id_form-0-email" class="block text-gray-700 text-sm font-bold mb-2"> email<span class="asteriskField">*</span> </label>
                <input
                    type="text"
                    name="form-0-email"
                    maxlength="30"
                    class="textinput textInput inputtext border appearance-none block rounded-lg border-gray-300 px-4 py-2 text-gray-700 w-full leading-normal bg-white focus:outline-none"
                    id="id_form-0-email"
                />
                <small id="hint_id_form-0-email" class="text-gray-600">Insert your email</small>
            </div>
            <div id="div_id_form-1-email" class="mb-3">
                <label for="id_form-1-email" class="block text-gray-700 text-sm font-bold mb-2"> email<span class="asteriskField">*</span> </label>
                <input
                    type="text"
                    name="form-1-email"
                    maxlength="30"
                    class="textinput textInput inputtext border appearance-none block rounded-lg border-gray-300 px-4 py-2 text-gray-700 w-full leading-normal bg-white focus:outline-none"
                    id="id_form-1-email"
                />
                <small id="hint_id_form-1-email" class="text-gray-600">Insert your email</small>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_buttons(self):
        form = CharFieldForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(Button("button", "Button"), Submit("submit", "Submit",), Reset("cancel", "Cancel"))
        html = render_crispy_form(form)
        expected_html = """
            <input type="button" name="button" value="Button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" id="button-id-button" />
            <input type="submit" name="submit" value="Submit" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" id="submit-id-submit" />
            <input type="reset" name="cancel" value="Cancel" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" id="reset-id-cancel" />
            """
        self.assertHTMLEqual(html, expected_html)

        form.helper.layout = Layout(
            Submit(
                "submit",
                "Submit",
                css_class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded",
            )
        )
        html = render_crispy_form(form)
        expected_html = """
            <input type="submit" name="submit" value="Submit" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" id="submit-id-submit" />
            """
        self.assertHTMLEqual(html, expected_html)

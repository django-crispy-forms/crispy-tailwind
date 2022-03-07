import django
from django.forms.models import formset_factory
from django.template import Template
from django.test import SimpleTestCase

from crispy_forms.bootstrap import InlineCheckboxes, InlineRadios
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

    def test_failing_CharField(self):
        form = CharFieldForm(data={"name": ""})
        form.helper = FormHelper()
        html = render_crispy_form(form)
        expected_html = """
            <form method="post">
                <div id="div_id_name" class="mb-3">
                    <label for="id_name" class="block text-gray-700 text-sm font-bold mb-2"> Name<span class="asteriskField">*</span> </label>
                    <input type="text" name="name" class="textinput textInput inputtext focus:outline-none w-full bg-white border-red-500 px-4 block rounded-lg text-gray-700 appearance-none py-2 leading-normal border" required id="id_name" />
                    <p id="error_1_id_name" class="text-red-500 text-xs italic"><strong>This field is required.</strong></p>
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
        label_for = ""
        if django.VERSION < (4, 0):
            label_for = "id_radio_0"
        expected_html = f"""
                <div id="div_id_radio" class="mb-3">
                    <label for="{label_for}" class="block font-bold mb-2 text-gray-700 text-sm"> Radio<span class="asteriskField">*</span> </label>
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
            Row(
                Column(Field("first_name"), Field("last_name"), css_class="px-2"),
                Column("email", css_class="px-2"),
            )
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
        label_for = ""
        if django.VERSION < (4, 0):
            label_for = "id_radio_0"
        expected_html = f"""
                <div id="div_id_radio" class="mb-3">
                    <label for="{label_for}" class=" block text-gray-700 text-sm font-bold mb-2 requiredField"> Radio<span class="asteriskField">*</span> </label>
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
        if django.VERSION < (3, 2):
            formset.non_form_errors = ["Please submit at most 2 forms."]
        html = render_crispy_form(formset)
        expected_html = """
            <div>
                <input type="hidden" name="name-TOTAL_FORMS" value="3" id="id_name-TOTAL_FORMS" /> <input type="hidden" name="name-INITIAL_FORMS" value="0" id="id_name-INITIAL_FORMS" />
                <input type="hidden" name="name-MIN_NUM_FORMS" value="0" id="id_name-MIN_NUM_FORMS" /> <input type="hidden" name="name-MAX_NUM_FORMS" value="0" id="id_name-MAX_NUM_FORMS" />
            </div>
            <div class="alert mb-4">
                <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2">
                    Non Form Errors
                </div>
                <div class="border border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
                    <ul>
                        <li>Please submit at most 2 forms.</li>
                    </ul>
                </div>
            </div>
            <div id="div_id_name-0-name" class="mb-3">
                <label for="id_name-0-name" class="block text-gray-700 text-sm font-bold mb-2"> Name<span class="asteriskField">*</span> </label>
                <input
                    type="text"
                    name="name-0-name"
                    value="test"
                    maxlength="3"
                    class="textinput textInput inputtext leading-normal bg-white w-full focus:outline-none text-gray-700 py-2 appearance-none rounded-lg px-4 block border border-red-500"
                    id="id_name-0-name"
                />
                <p id="error_1_id_name-0-name" class="text-red-500 text-xs italic"><strong>Ensure this value has at most 3 characters (it has 4).</strong></p>
            </div>
            <div id="div_id_name-1-name" class="mb-3">
                <label for="id_name-1-name" class="block text-gray-700 text-sm font-bold mb-2"> Name<span class="asteriskField">*</span> </label>
                <input
                    type="text"
                    name="name-1-name"
                    maxlength="3"
                    class="textinput textInput inputtext leading-normal bg-white w-full focus:outline-none text-gray-700 py-2 appearance-none rounded-lg px-4 block border border-gray-300"
                    id="id_name-1-name"
                />
            </div>
            <div id="div_id_name-2-name" class="mb-3">
                <label for="id_name-2-name" class="block text-gray-700 text-sm font-bold mb-2"> Name<span class="asteriskField">*</span> </label>
                <input
                    type="text"
                    name="name-2-name"
                    maxlength="3"
                    class="textinput textInput inputtext leading-normal bg-white w-full focus:outline-none text-gray-700 py-2 appearance-none rounded-lg px-4 block border border-gray-300"
                    id="id_name-2-name"
                />
            </div>
             """
        self.assertHTMLEqual(html, expected_html)

    def test_formset_with_form_tag(self):
        SampleFormSet = formset_factory(SampleForm, extra=2)
        formset = SampleFormSet()
        formset.helper = FormHelper()
        formset.helper.form_tag = True
        formset.helper.layout = Layout("email")
        html = render_crispy_form(formset)
        expected_html = """
            <form method="post">
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
                        class="textinput textInput inputtext border border-gray-300 py-2 px-4 block rounded-lg appearance-none w-full leading-normal bg-white text-gray-700 focus:outline-none"
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
                        class="textinput textInput inputtext border border-gray-300 py-2 px-4 block rounded-lg appearance-none w-full leading-normal bg-white text-gray-700 focus:outline-none"
                        id="id_form-1-email"
                    />
                    <small id="hint_id_form-1-email" class="text-gray-600">Insert your email</small>
                </div>
            </form>
            """
        self.assertHTMLEqual(html, expected_html)

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

    def test_div(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = Layout(Div("email", "name", css_class="test class"))
        html = render_crispy_form(form)
        expected_html = """
            <div class="test class">
                <div id="div_id_email" class="mb-3">
                    <label for="id_email" class="block text-gray-700 text-sm font-bold mb-2"> email<span class="asteriskField">*</span> </label>
                    <input
                        type="text"
                        name="email"
                        maxlength="30"
                        class="textinput textInput inputtext appearance-none border bg-white focus:outline-none py-2 w-full text-gray-700 border-gray-300 leading-normal block px-4 rounded-lg"
                        required
                        id="id_email"
                    />
                    <small id="hint_id_email" class="text-gray-600">Insert your email</small>
                </div>
            </div>
            """
        self.assertHTMLEqual(html, expected_html)

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
        html = render_crispy_form(form)
        expected_html = """
            <fieldset>
                <legend class="block text-gray-700 font-bold mb-2">Text for the legend</legend>
                <div id="div_id_is_company" class="mb-3">
                    <label for="id_is_company" class="block text-gray-700 text-sm font-bold mb-2">
                        company
                    </label>
                    <input type="checkbox" name="is_company" class=" checkboxinput" id="id_is_company" />
                </div>
                <div id="div_id_email" class="mb-3">
                    <label for="id_email" class="block text-gray-700 text-sm font-bold mb-2"> email<span class="asteriskField">*</span> </label>
                    <input
                        type="text"
                        name="email"
                        maxlength="30"
                        class="textinput textInput inputtext text-gray-700 py-2 w-full px-4 block focus:outline-none leading-normal bg-white rounded-lg border border-gray-300 appearance-none"
                        required
                        id="id_email"
                    />
                    <small id="hint_id_email" class="text-gray-600">Insert your email</small>
                </div>
            </fieldset>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_non_form_errors(self):
        form = SampleForm(data={})
        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.form_error_title = "Form Error Title"
        form.helper.layout = Layout("password1", "password2")
        html = render_crispy_form(form)
        expected_html = """
        <div class="alert mb-4">
            <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2">
                Form Error Title
            </div>
            <div class="border border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
                <ul>
                    <li>Passwords dont match</li>
                </ul>
            </div>
        </div>
        <div id="div_id_password1" class="mb-3">
            <label for="id_password1" class="block text-gray-700 text-sm font-bold mb-2"> password<span class="asteriskField">*</span> </label>
            <input
                type="password"
                name="password1"
                maxlength="30"
                class="passwordinput focus:outline-none rounded-lg border appearance-none text-gray-700 leading-normal block px-4 py-2 w-full bg-white border-red-500"
                required
                id="id_password1"
            />
            <p id="error_1_id_password1" class="text-red-500 text-xs italic"><strong>This field is required.</strong></p>
        </div>
        <div id="div_id_password2" class="mb-3">
            <label for="id_password2" class="block text-gray-700 text-sm font-bold mb-2"> re-enter password<span class="asteriskField">*</span> </label>
            <input
                type="password"
                name="password2"
                maxlength="30"
                class="passwordinput focus:outline-none rounded-lg border appearance-none text-gray-700 leading-normal block px-4 py-2 w-full bg-white border-red-500"
                required
                id="id_password2"
            />
            <p id="error_1_id_password2" class="text-red-500 text-xs italic"><strong>This field is required.</strong></p>
        </div>
        """
        self.assertHTMLEqual(html, expected_html)

    def test_select(self):
        form = SelectForm(data={"tos_accepted": "accepted"})
        form.helper = FormHelper()
        form.helper.form_tag = False
        html = render_crispy_form(form)
        expected_html = """
        <div id="div_id_tos_accepted" class="mb-3">
            <label for="id_tos_accepted" class="block text-gray-700 text-sm font-bold mb-2"> terms of service<span class="asteriskField">*</span> </label>
            <div class="mb-3">
                <div class="relative">
                    <select class="bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700" name="tos_accepted">
                        <option value="accepted" selected>Accepted</option>
                        <option value="not_accepted">Not accepted</option>
                    </select>
                    <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                        <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" /></svg>
                    </div>
                </div>
            </div>
        </div>
        """
        self.assertHTMLEqual(html, expected_html)

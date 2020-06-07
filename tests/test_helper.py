from django.template import Context, Template
from django.test import SimpleTestCase

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Field
from crispy_forms.utils import render_crispy_form

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
        <form  method="post" > 
        <div id="div_id_name" class="mb-3"> <label for="id_name" class="block font-bold mb-2 text-gray-700 text-sm">
            Name<span class="asteriskField">*</span> 
            </label> 
            <input type="text" name="name" class="textinput textInput inputtext block bg-white rounded-lg leading-normal border-gray-300 px-4 appearance-none border focus:outline-none w-full py-2 text-gray-700" required id="id_name"> 
            </div> 
            </form>"""
        self.assertHTMLEqual(html, expected_html)

    def test_password(self):
        form = PasswordFieldForm()
        form.helper = FormHelper()
        html = render_crispy_form(form)
        expected_html = """
        <form  method="post" > 
        <div id="div_id_password" class="mb-3"> 
        <label for="id_password" class="block font-bold mb-2 text-gray-700 text-sm">
            Password<span class="asteriskField">*</span> </label> 
            <input type="password" name="password" class="passwordinput bg-white text-gray-700 w-full px-4 border py-2 border-gray-300 block rounded-lg focus:outline-none leading-normal appearance-none" required id="id_password"> 
            </div> </form>"""
        self.assertHTMLEqual(html, expected_html)

    def test_radio(self):
        form = RadioForm()
        form.helper = FormHelper()
        html = render_crispy_form(form)
        expected_html = """
        <form  method="post" > <div id="div_id_radio" class="mb-3"> <label for="id_radio_0" class="block font-bold mb-2 text-gray-700 text-sm">
            Radio<span class="asteriskField">*</span> </label> <div class="mb-3"> 
            <label for="id_radio_1" class="block text-gray-700 mr-3"> <input type="radio" class="" name="radio" id="id_radio_1" value="blue" >
        Blue
    </label> <label for="id_radio_2" class="block text-gray-700 mr-3"> <input type="radio" class="" name="radio" id="id_radio_2" value="green" >
        Green
    </label> </div> </div> </form>
    """
        self.assertHTMLEqual(html, expected_html)

    def test_multiple_checkbox(self):
        form = CheckboxMultiple()
        form.helper = FormHelper()
        html = render_crispy_form(form)
        expected_html = """
<form  method="post" > <div id="div_id_radio" class="mb-3"> <label for="" class="block font-bold mb-2 text-gray-700 text-sm">
            Radio<span class="asteriskField">*</span> </label> <div class="mb-3"> <div class="mr-3"> <label class="block text-gray-700" for="id_radio_1"> <input type="checkbox" class="" name="radio" id="id_radio_1" value="blue" >
            Blue
        </label> </div> <div class="mr-3"> <label class="block text-gray-700" for="id_radio_2"> <input type="checkbox" class="" name="radio" id="id_radio_2" value="green" >
            Green
        </label> </div>

</div> </div> </form>
    """
        self.assertHTMLEqual(html, expected_html)

    def test_crispy_layout(self):
        form = SampleForm
        form.helper = FormHelper()
        form.helper.layout = Layout("is_company", "first_name")
        html = render_crispy_form(form)
        expected_html = """
<form  method="post" > <div id="div_id_is_company" class="mb-3"> <label for="id_is_company" class="block font-bold mb-2 text-gray-700 text-sm">
            company
        </label> <input type="checkbox" name="is_company" class="checkboxinput " id="id_is_company"> </div> <div id="div_id_first_name" class="mb-3"> <label for="id_first_name" class="block font-bold mb-2 text-gray-700 text-sm">
            first name<span class="asteriskField">*</span> </label> <input type="text" name="first_name" maxlength="5" class="textinput textInput inputtext rounded-lg leading-normal border text-gray-700 w-full block border-gray-300 appearance-none bg-white focus:outline-none px-4 py-2" required id="id_first_name"> </div> </form>
            """
        self.assertHTMLEqual(html, expected_html)

    def test_col(self):
        form = SampleForm()
        form.helper = FormHelper()
        form.helper.layout = Layout(
            Column(
                Field('first_name', wrapper_class='px-2'),
                Field('last_name', wrapper_class='px-2'),
            )
        )
        html = render_crispy_form(form)
        expected_html = """
        <form  method="post" > <div 
     class="flex flex-row" > <div id="div_id_first_name" class="px-2 mb-3"> 
     <label for="id_first_name" class="block text-gray-700 text-sm font-bold mb-2">
            first name<span class="asteriskField">*</span> </label> 
    <input type="text" name="first_name" maxlength="5" class="textinput textInput inputtext focus:outline-none block rounded-lg appearance-none leading-normal border-gray-300 bg-white border w-full py-2 text-gray-700 px-4" required id="id_first_name"> </div> <div id="div_id_last_name" class="px-2 mb-3"> <label for="id_last_name" class="block text-gray-700 text-sm font-bold mb-2">
            last name<span class="asteriskField">*</span> </label> 
    <input type="text" name="last_name" maxlength="5" class="textinput textInput inputtext focus:outline-none block rounded-lg appearance-none leading-normal border-gray-300 bg-white border w-full py-2 text-gray-700 px-4" required id="id_last_name"> </div> </div> </form>
    """
        self.assertHTMLEqual(html, expected_html)
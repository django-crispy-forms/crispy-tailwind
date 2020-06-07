from django.template import Context, Template
from django.test import SimpleTestCase

from crispy_forms.helper import FormHelper
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
        <div id="div_id_name" class=""> <label for="id_name" class="">
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
        <div id="div_id_password" class=""> 
        <label for="id_password" class="">
            Password<span class="asteriskField">*</span> </label> 
            <input type="password" name="password" class="passwordinput bg-white text-gray-700 w-full px-4 border py-2 border-gray-300 block rounded-lg focus:outline-none leading-normal appearance-none" required id="id_password"> 
            </div> </form>"""
        self.assertHTMLEqual(html, expected_html)

    def test_radio(self):
        form = RadioForm()
        form.helper = FormHelper()
        html = render_crispy_form(form)
        expected_html = """
        <form  method="post" > <div id="div_id_radio" class=""> <label for="id_radio_0" class="">
            Radio<span class="asteriskField">*</span> </label> <div class=""> 
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
<form  method="post" > <div id="div_id_radio" class=""> <label for="" class="">
            Radio<span class="asteriskField">*</span> </label> <div class=""> <div class="mr-3"> <label class="block text-gray-700" for="id_radio_1"> <input type="checkbox" class="" name="radio" id="id_radio_1" value="blue" >
            Blue
        </label> </div> <div class="mr-3"> <label class="block text-gray-700" for="id_radio_2"> <input type="checkbox" class="" name="radio" id="id_radio_2" value="green" >
            Green
        </label> </div>

</div> </div> </form>
    """
        self.assertHTMLEqual(html, expected_html)

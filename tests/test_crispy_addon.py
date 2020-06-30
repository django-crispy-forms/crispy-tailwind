from django.template import Context, Template
from django.test import SimpleTestCase

from .forms import SampleForm


class CrispyHelperTests(SimpleTestCase):
    maxDiff = None

    def test_crispy_addon(self):
        template = Template(
            """
            {% load tailwind_field %}
            {% crispy_addon form.last_name prepend="$" append=".00" %}
            """
        )
        html = template.render(Context({"form": SampleForm()}))
        expected_html = """
        <div id="div_id_last_name" class="mb-3">
            <label for="id_last_name" class="block text-gray-700 text-sm font-bold mb-2"> last name<span class="asteriskField">*</span> </label>
            <div class="">
                <div class="flex">
                    <span class="border-gray-300 border rounded-lg rounded-r-none px-3 bg-gray-200 text-gray-800 flex items-center">$</span>
                    <input type="text" name="last_name" maxlength="5" class="textinput textInput inputtext border border-gray-300 px-4 py-2 w-full focus:outline-none text-gray-700 border-r-0 leading-normal" required id="id_last_name" />
                    <span class="border-gray-300 border rounded-lg rounded-l-none px-3 bg-gray-200 text-gray-800 flex items-center">.00</span>
                </div>
            </div>
        </div>
        """
        self.assertHTMLEqual(html, expected_html)

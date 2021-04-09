import django
from django.forms import formset_factory
from django.test import SimpleTestCase

from crispy_forms.helper import FormHelper
from crispy_forms.utils import render_crispy_form
from crispy_tailwind.layout import Submit

from .forms import SampleForm, ShortCharFieldForm


class CrispyHelperTests(SimpleTestCase):
    maxDiff = None

    def test_table_inline_formset(self):
        SampleFormSet = formset_factory(SampleForm, extra=2)
        formset = SampleFormSet()
        formset.helper = FormHelper()
        formset.helper.form_tag = False
        formset.helper.add_input(Submit("submit", "submit"))
        formset.helper.template = "tailwind/table_inline_formset.html"
        html = render_crispy_form(formset)
        expected_html = """
        <div>
            <input type="hidden" name="form-TOTAL_FORMS" value="2" id="id_form-TOTAL_FORMS" /> <input type="hidden" name="form-INITIAL_FORMS" value="0" id="id_form-INITIAL_FORMS" />
            <input type="hidden" name="form-MIN_NUM_FORMS" value="0" id="id_form-MIN_NUM_FORMS" /> <input type="hidden" name="form-MAX_NUM_FORMS" value="1000" id="id_form-MAX_NUM_FORMS" />
        </div>
        <table class="table-auto">
            <thead>
                <tr>
                    <th for="id_form-0-is_company" class="px-4 py-2">
                        company
                    </th>
                    <th for="id_form-0-email" class="px-4 py-2">email<span class="asteriskField">*</span></th>
                    <th for="id_form-0-password1" class="px-4 py-2">password<span class="asteriskField">*</span></th>
                    <th for="id_form-0-password2" class="px-4 py-2">re-enter password<span class="asteriskField">*</span></th>
                    <th for="id_form-0-first_name" class="px-4 py-2">first name<span class="asteriskField">*</span></th>
                    <th for="id_form-0-last_name" class="px-4 py-2">last name<span class="asteriskField">*</span></th>
                    <th for="id_form-0-datetime_field" class="px-4 py-2">date time<span class="asteriskField">*</span></th>
                    <th for="id_form-0-tos_accepted" class="px-4 py-2">terms of service<span class="asteriskField">*</span></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td id="div_id_form-0-is_company" class="border px-4 py-2"><input type="checkbox" name="form-0-is_company" class=" checkboxinput" id="id_form-0-is_company" /></td>
                    <td id="div_id_form-0-email" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-0-email"
                            maxlength="30"
                            class="textinput textInput inputtext w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-0-email"
                        />
                        <small id="hint_id_form-0-email" class="text-gray-600">Insert your email</small>
                    </td>
                    <td id="div_id_form-0-password1" class="border px-4 py-2">
                        <input
                            type="password"
                            name="form-0-password1"
                            maxlength="30"
                            class="passwordinput w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-0-password1"
                        />
                    </td>
                    <td id="div_id_form-0-password2" class="border px-4 py-2">
                        <input
                            type="password"
                            name="form-0-password2"
                            maxlength="30"
                            class="passwordinput w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-0-password2"
                        />
                    </td>
                    <td id="div_id_form-0-first_name" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-0-first_name"
                            maxlength="5"
                            class="textinput textInput inputtext w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-0-first_name"
                        />
                    </td>
                    <td id="div_id_form-0-last_name" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-0-last_name"
                            maxlength="5"
                            class="textinput textInput inputtext w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-0-last_name"
                        />
                    </td>
                    <td id="div_id_form-0-datetime_field" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-0-datetime_field_0"
                            class="dateinput border border-gray-300 text-gray-700 focus:outline-none px-4 mr-2 bg-white focus:outline leading-normal rounded-lg py-2 appearance-none"
                            id="id_form-0-datetime_field_0"
                        />
                        <input
                            type="text"
                            name="form-0-datetime_field_1"
                            class="timeinput border border-gray-300 text-gray-700 focus:outline-none px-4 mr-2 bg-white focus:outline leading-normal rounded-lg py-2 appearance-none"
                            id="id_form-0-datetime_field_1"
                        />
                    </td>
                    <td id="div_id_form-0-tos_accepted" class="border px-4 py-2">
                        <div class="border px-4 py-2">
                            <div class="relative">
                                <select class="bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700" name="form-0-tos_accepted">
                                    <option value="accepted">Accepted</option>
                                    <option value="not_accepted">Not accepted</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" /></svg>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td id="div_id_form-1-is_company" class="border px-4 py-2"><input type="checkbox" name="form-1-is_company" class=" checkboxinput" id="id_form-1-is_company" /></td>
                    <td id="div_id_form-1-email" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-1-email"
                            maxlength="30"
                            class="textinput textInput inputtext w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-1-email"
                        />
                        <small id="hint_id_form-1-email" class="text-gray-600">Insert your email</small>
                    </td>
                    <td id="div_id_form-1-password1" class="border px-4 py-2">
                        <input
                            type="password"
                            name="form-1-password1"
                            maxlength="30"
                            class="passwordinput w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-1-password1"
                        />
                    </td>
                    <td id="div_id_form-1-password2" class="border px-4 py-2">
                        <input
                            type="password"
                            name="form-1-password2"
                            maxlength="30"
                            class="passwordinput w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-1-password2"
                        />
                    </td>
                    <td id="div_id_form-1-first_name" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-1-first_name"
                            maxlength="5"
                            class="textinput textInput inputtext w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-1-first_name"
                        />
                    </td>
                    <td id="div_id_form-1-last_name" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-1-last_name"
                            maxlength="5"
                            class="textinput textInput inputtext w-full border border-gray-300 focus:outline-none text-gray-700 px-4 bg-white leading-normal rounded-lg block py-2 appearance-none"
                            id="id_form-1-last_name"
                        />
                    </td>
                    <td id="div_id_form-1-datetime_field" class="border px-4 py-2">
                        <input
                            type="text"
                            name="form-1-datetime_field_0"
                            class="dateinput border border-gray-300 text-gray-700 focus:outline-none px-4 mr-2 bg-white focus:outline leading-normal rounded-lg py-2 appearance-none"
                            id="id_form-1-datetime_field_0"
                        />
                        <input
                            type="text"
                            name="form-1-datetime_field_1"
                            class="timeinput border border-gray-300 text-gray-700 focus:outline-none px-4 mr-2 bg-white focus:outline leading-normal rounded-lg py-2 appearance-none"
                            id="id_form-1-datetime_field_1"
                        />
                    </td>
                    <td id="div_id_form-1-tos_accepted" class="border px-4 py-2">
                        <div class="border px-4 py-2">
                            <div class="relative">
                                <select class="bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700" name="form-1-tos_accepted">
                                    <option value="accepted">Accepted</option>
                                    <option value="not_accepted">Not accepted</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" /></svg>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="mt-3">
            <div class="form-group">
                <div class=""><input type="submit" name="submit" value="submit" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" id="submit-id-submit" /></div>
            </div>
        </div>

        """
        self.assertHTMLEqual(html, expected_html)

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
        if django.VERSION < (3, 2):
            formset.non_form_errors = ["Please submit at most 2 forms."]
        html = render_crispy_form(formset)
        expected_html = """
        <form method="post">
            <div> <input type="hidden" name="name-TOTAL_FORMS" value="3" id="id_name-TOTAL_FORMS"> <input type="hidden" name="name-INITIAL_FORMS" value="0" id="id_name-INITIAL_FORMS"> <input type="hidden" name="name-MIN_NUM_FORMS" value="0" id="id_name-MIN_NUM_FORMS">        <input type="hidden" name="name-MAX_NUM_FORMS" value="0" id="id_name-MAX_NUM_FORMS"> </div>
            <div class="alert mb-4">
                <div class="border border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
                    <ul>
                        <li>Please submit at most 2 forms.</li>
                    </ul>
                </div>
            </div>
            <table class="table-auto">
                <thead>
                    <tr>
                        <th for="id_name-0-name" class="px-4 py-2">
                            Name<span class="asteriskField">*</span> </th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td id="div_id_name-0-name" class="border px-4 py-2"> <input type="text" name="name-0-name" value="test" maxlength="3" class="textinput textInput inputtext bg-white px-4 w-full appearance-none border py-2 focus:outline-none border-red-500 block rounded-lg leading-normal text-gray-700" id="id_name-0-name">
                            <p id="error_1_id_name-0-name" class="text-red-500 text-xs italic"><strong>Ensure this value has at most 3 characters (it has 4).</strong></p>
                        </td>
                    </tr>
                    <tr>
                        <td id="div_id_name-1-name" class="border px-4 py-2"> <input type="text" name="name-1-name" maxlength="3" class="textinput textInput inputtext bg-white px-4 w-full appearance-none border py-2 focus:outline-none border-gray-300 block rounded-lg leading-normal text-gray-700" id="id_name-1-name">                    </td>
                    </tr>
                    <tr>
                        <td id="div_id_name-2-name" class="border px-4 py-2"> <input type="text" name="name-2-name" maxlength="3" class="textinput textInput inputtext bg-white px-4 w-full appearance-none border py-2 focus:outline-none border-gray-300 block rounded-lg leading-normal text-gray-700" id="id_name-2-name">                    </td>
                    </tr>
                </tbody>
            </table>
            <div class="mt-3">
                <div class="form-group">
                    <div class=""> <input type="submit" name="submit" value="submit" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" id="submit-id-submit" /> </div>
                </div>
            </div>
        </form>
        """
        self.assertHTMLEqual(html, expected_html)

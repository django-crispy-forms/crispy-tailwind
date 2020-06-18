from crispy_forms.bootstrap import Alert
from crispy_forms.layout import BaseInput


class Submit(BaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag::
        submit = Submit('Search the Site', 'search this site')
    .. note:: The first argument is also slugified and turned into the id for the submit button.

    This is a customised version for Tailwind to add Tailwind CSS style by default
    """

    input_type = "submit"

    def __init__(self, *args, css_class=None, **kwargs):
        if css_class is None:
            self.field_classes = "bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class Reset(BaseInput):
    """
    Used to create a Reset button input descriptor for the {% crispy %} template tag::
        reset = Reset('Reset This Form', 'Revert Me!')
    .. note:: The first argument is also slugified and turned into the id for the reset.

    This is a customised version for Tailwind to add Tailwind CSS style by default
    """

    input_type = "reset"

    def __init__(self, *args, css_class=None, **kwargs):
        if css_class is None:
            self.field_classes = "bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class Button(BaseInput):
    """
    Used to create a button descriptor for the {% crispy %} template tag::
        submit = Button('Search the Site', 'search this site')
    .. note:: The first argument is also slugified and turned into the id for the submit button.

    This is a customised version for Tailwind to add Tailwind CSS style by default
    """

    input_type = "button"

    def __init__(self, *args, css_class=None, **kwargs):
        if css_class is None:
            self.field_classes = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class Alert(Alert):
    css_class = ""

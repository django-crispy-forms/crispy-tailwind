from django import forms


class SampleForm(forms.Form):
    is_company = forms.CharField(label="company", required=False, widget=forms.CheckboxInput())
    email = forms.EmailField(
        label="email", max_length=30, required=True, widget=forms.TextInput(), help_text="Insert your email"
    )
    password1 = forms.CharField(label="password", max_length=30, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(label="re-enter password", max_length=30, required=True, widget=forms.PasswordInput())
    first_name = forms.CharField(label="first name", max_length=5, required=True, widget=forms.TextInput())
    last_name = forms.CharField(label="last name", max_length=5, required=True, widget=forms.TextInput())
    datetime_field = forms.SplitDateTimeField(label="date time", widget=forms.SplitDateTimeWidget())
    tos_accepted = forms.ChoiceField(
        label="terms of service",
        widget=forms.Select(),
        choices=(("accepted", "Accepted"), ("not_accepted", "Not accepted")),
    )

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get("password1", None)
        password2 = self.cleaned_data.get("password2", None)
        if not password1 and not password2 or password1 != password2:
            raise forms.ValidationError("Passwords dont match")

        return self.cleaned_data


class CharFieldForm(forms.Form):

    name = forms.CharField(required=True)


class ShortCharFieldForm(forms.Form):
    name = forms.CharField(required=True, max_length=3)


class PasswordFieldForm(forms.Form):

    password = forms.CharField(widget=forms.PasswordInput)


class RadioForm(forms.Form):
    choices = [
        ("blue", "Blue"),
        ("green", "Green"),
    ]
    radio = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)


class CheckboxMultiple(forms.Form):
    choices = [
        ("blue", "Blue"),
        ("green", "Green"),
    ]
    checkbox = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices)


class SelectForm(forms.Form):
    tos_accepted = forms.ChoiceField(
        label="terms of service",
        widget=forms.Select(),
        choices=(("accepted", "Accepted"), ("not_accepted", "Not accepted")),
    )


class CustomTextWidget(forms.TextInput):
    pass


class CustomTextWidgetForm(forms.Form):
    first_name = forms.CharField(widget=CustomTextWidget())
    last_name = forms.CharField(widget=CustomTextWidget(attrs={"class": "custom-css"}))

from django import forms


class UserForm(forms.Form):
    login = forms.CharField(label="Username", required=True)
    password = forms.CharField(label="Password", required=True)


class UserForm2(forms.Form):
    code = forms.CharField(label="Your code:", required=True)
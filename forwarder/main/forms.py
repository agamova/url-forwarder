from django import forms


class ForwarderForm(forms.Form):
    access_code = forms.CharField(max_length=100, label='Enter access code')

from django import forms


class ForwarderForm(forms.Form):
    access_code = forms.CharField(max_length=20, label='Access code')

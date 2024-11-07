from django import forms

class URLForm(forms.Form):
    url = forms.URLField(
        label='Enter Your Website URL',
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'})
    )

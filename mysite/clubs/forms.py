from django import forms

class DocumentForm(forms.Form):
	docfile = forms.ImageField(
		label = 'Select an image'
		)
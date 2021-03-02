from django import forms
from .models import ( Headword, POS, Meaning)  

class HeadwordForm(forms.ModelForm):
	class Meta:
		model = Headword 
		fields = "__all__"





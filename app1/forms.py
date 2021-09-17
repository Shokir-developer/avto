from django import forms
from .models import CarsGM

class CarsForm(forms.ModelForm):
	class Meta:
		model = CarsGM
		fields = '__all__'
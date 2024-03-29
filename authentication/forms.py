from django import forms
from django.contrib.auth.models import User

class UserRegister(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email', 'password']

		widget = {
		'password': forms.PasswordInput()
		}
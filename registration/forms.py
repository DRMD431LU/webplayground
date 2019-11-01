from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ValidationEmail():
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError(f"ya existe un usuario con la direccion: {email}")
		return email

class UserCreationFormWithEmail(ValidationEmail,UserCreationForm):
	email = forms.EmailField(required=True, help_text="Requerido, 254 max")

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class PofileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar','bio', 'link']
		widgets = {
				'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
				'bio':forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Bio'}),
				'link':forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
				}


class EmailForm(forms.ModelForm):
	email = forms.EmailField(required=True, help_text="Requerido, 254 max")
	class Meta:
		model = User
		fields = ['email']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if 'email' in self.changed_data:
			if User.objects.filter(email=email).exists():
				raise forms.ValidationError(f"ya existe un usuario con la direccion: {email}")
		return email
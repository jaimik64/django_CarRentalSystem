from django import forms
from .models import User


# creating a form
class UserForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = User
		# specify fields to be used
		fields = ('username', 'firstname', 'lastname')

		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        }

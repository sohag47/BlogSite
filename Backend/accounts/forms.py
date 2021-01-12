from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import ExtraUserInfo

#from accounts.models import ExtraUserInfo
class SignUpForm(UserCreationForm):
    class Meta(object):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter Your First Name",
                    'required': 'true'

                }
            ),
            'last_name': forms.TextInput(
                attrs={

                    'placeholder': "Enter Your Last Name",
                    'required': 'true'

                }
            ),
            'username': forms.TextInput(
                attrs={

                    'placeholder': "Enter User Name ",
                    'required': 'true'

                }
            ),
            'email': forms.EmailInput(
                attrs={

                    'placeholder': "Enter Your Email",
                    'required': 'true'

                }
            ),
            'password1': forms.PasswordInput(
                attrs={

                    'placeholder': "Enter First Password",
                    'required': 'true'

                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': "Enter Confirm Password",
                    'required': 'true'

                }
            ),
        }


# Login form
class LogInForm(AuthenticationForm):
    class Meta(object):
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter User Name",
                    'required': 'true'

                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Your Password",
                    'required': 'true'

                }
            ),
        }

class ExtraUserInfoForm(forms.ModelForm):
    class Meta:
        model = ExtraUserInfo
        fields = ['profile_img', 'country', 'language', 'description']

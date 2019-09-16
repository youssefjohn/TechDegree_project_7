from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, AuthenticationForm
import datetime
from .models import More_User_Details



def bio_check(value):
    if len(value) < 14:
        raise forms.ValidationError("Please enter more information.")


class Register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class Login_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class More_User_Details_Form(forms.ModelForm):
    dob = forms.DateField(input_formats=['%Y-%m-%d','%m/%d/%Y', '%m/%d/%y'])
                                      #'2006-10-25' '10/25/2006' '10/25/06'

    bio = forms.CharField(widget=forms.Textarea,
                          validators=[bio_check])

    class Meta:
        model=More_User_Details
        fields=('dob','bio', 'avatar', 'city', 'hobby')


class Edit_Profile_Form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')


        if password != password_confirm:
            raise forms.ValidationError("Passwords must match!!!")

    class Meta:
        model=User
        fields=('username', 'email', 'password', 'password_confirm')


class Edit_Password_Form(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'



# class Edit_Password_Form(forms.ModelForm):
#     old_password = forms.CharField(widget=forms.PasswordInput())                            # This is my attempt at used 'check_password().
#     new_password = forms.CharField(widget=forms.PasswordInput())                            # For the purpose of time, I will use django's built in password change form. Aboove.
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#
#     def clean(self):
#         cleaned_data = super().clean()
#         old_password = cleaned_data.get('old_password')
#         new_password = cleaned_data.get('new_password')
#         confirm_password = cleaned_data.get('confirm_password')
#
#         if new_password != confirm_password:
#             raise forms.ValidationError('Passwords must match!')
#
#
#     def clean_old_password(self):
#         old_password = self.cleaned_data.get('old_password')
#         if self.user.check_password(old_password):
#             return old_password
#         else:
#             raise forms.ValidationError("Does not match current password")
#
#
#
#     class Meta:
#         model=User
#         fields = ('old_password', 'new_password', 'confirm_password')






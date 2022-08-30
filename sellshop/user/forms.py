from django import forms
# from user.models import BillingAddress
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _

USER = get_user_model()


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'New Password'
            }))
    new_password2 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }))


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }), max_length=255)
    

# class AddresForm(forms.ModelForm):
    
#     class Meta:
#         model = BillingAddress
#         fields = (
#             'first_name',
#             'last_name',
#             'email',
#             'country',
#             'address',
#             'town',
#             'mobile_phone',
#             'information',
#             'reference',
#         )
#         widgets = {
#             'first_name': forms.TextInput(attrs={
#                 'placeholder': 'First Name'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'placeholder': 'Last Name'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'placeholder': 'Email Address'
#             }),
#             'country': forms.Select(attrs={
#                 'placeholder': 'Country',
#                 'class': 'form-control'
#             }),
#             'address': forms.TextInput(attrs={
#                 'placeholder': 'Address'
#             }),
#             'town': forms.Select(attrs={
#                 'placeholder': 'Town/City',
#                 'class': 'form-control'
#             }),
#             'mobile_phone': forms.NumberInput(attrs={
#                 'placeholder': 'Mobile phone'
#             }),
#             'information': forms.Textarea(attrs={
#                 'placeholder': 'Additional information',
#                 'rows': 2
#             }),
#             'reference': forms.TextInput()
#         }

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }))

    class Meta:
        model = USER
        fields = (
            'username',
            "first_name",
            "last_name",
            'email',
            'phone_number',
            'password',
            'confirm_password',
            'birthdate',
            'sex',
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username here'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name here'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name here'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            'sex': forms.Select(attrs={
                'placeholder':'MR or MRs', 
                'class': 'form-control', 
            }),
            'birthdate': forms.DateInput(attrs={
                'placeholder':'Birth Date', 
                'class': 'form-control',
                'type': 'date',                                                                 
            })
        }

    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("Please make sure your passwords match")
        return super().clean()


class UpdatePersonalInfoForm(forms.ModelForm):
    class Meta:
        model = USER
        fields = (
            "first_name",
            "last_name",
            'email',
            'birthdate',
            'sex',
        )
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name here'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name here'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'birthdate': forms.DateInput(attrs={
                'placeholder':'Birth Date', 
                'class': 'form-control',
                'type': 'date',                                                                 
            }),
            'sex': forms.Select(attrs={
                'placeholder':'MR or MRs', 
                'class': 'form-control', 
            }),
        }



class LoginForm(AuthenticationForm):
    class Meta:
        model = USER
        fields = (
            'username',
            'password',
        )
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 
    'class': 'form-control',
        'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"),
                                   widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Old Password'
                                    }))
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'Confirm Password'}))




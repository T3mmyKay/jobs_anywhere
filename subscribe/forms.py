from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError("Invalid Last Name")
    return value


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': _('Enter First Name'),
            'last_name': _('Enter Last Name'),
            'email': _('Enter Email'),
        }
        error_messages = {
            'first_name': {
                'required': _("First Name is required"),
            },
            'last_name': {
                'required': _("Last Name is required"),
            },
            'email': {
                'required': _("Email is required"),
            },
        }

# class SubscribeForm(forms.ModelForm):
# first_name = forms.CharField(max_length=100, label="First Name", required=True)
# last_name = forms.CharField(max_length=100, label="Last Name", required=True, disabled=False,
#                             validators=[validate_comma])
# email = forms.EmailField(label="Email", required=True)

# def clean_first_name(self):
#     first_name = self.cleaned_data['first_name']
#     if len(first_name) < 3:
#         raise forms.ValidationError("First name must be at least 3 characters long")
#     elif "," in first_name:
#         raise forms.ValidationError("Invalid character in first name")
#     return first_name

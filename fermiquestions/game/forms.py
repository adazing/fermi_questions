from django.forms import ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ConfirmGameResetForm(forms.Form):
    confirm = forms.BooleanField(required = True)

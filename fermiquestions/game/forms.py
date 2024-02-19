from django.forms import ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AnswerForm(forms.Form):
    answer = forms.IntegerField(required = True)
    # question_id = forms.IntegerField(required = True)

from django.forms import ModelForm
from django import forms
from .models import *

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = [
            "name",
        ]
        labels = {
            "name" : "Repository Name",
        }

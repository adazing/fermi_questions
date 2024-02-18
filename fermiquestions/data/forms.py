from django.forms import ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = [
            "name",
        ]
        labels = {
            "name" : "Repository Name",
        }

class ConfirmDeleteForm(forms.Form):
    confirm = forms.BooleanField(required = True)

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            "query",
            "answer",
        ]
    

# multiple file stuff
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

#file extension validator
def validate_file_extension(value):
    if not value.name.endswith('.txt') and not value.name.endswith('.text'):
        raise ValidationError(u'Wrong file extension! Make sure the file is .txt or .text.')

class AddFilesToRepositoryForm(forms.Form):
    file_field = MultipleFileField(label = "", validators=[validate_file_extension])


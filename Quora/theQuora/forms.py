from .models import Answer
from django import forms



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(),
            'body': forms.Textarea(),

        }

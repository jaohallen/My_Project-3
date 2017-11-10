from django import forms

from polls.models import Question


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

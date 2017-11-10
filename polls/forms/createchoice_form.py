from django import forms

from polls.models import Choice


class CreateChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        exclude = ('question', 'votes')

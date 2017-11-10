from django import forms

from polls.models import Choice


class CreateChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = '__all__'

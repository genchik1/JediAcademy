from django import forms

from .models import Сandidate, Answer


class СandidateForm(forms.ModelForm):
    class Meta:
        model = Сandidate
        fields = ("name", "age", "habitat_planet", "email",)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("qestions",)
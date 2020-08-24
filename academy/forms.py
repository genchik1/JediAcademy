from django import forms

from .models import Сandidate


class СandidateForm(forms.ModelForm):
    # name = forms
    # age
    # habitat_planet
    # email
    class Meta:
        model = Сandidate
        fields = ("name", "age", "habitat_planet", "email",)

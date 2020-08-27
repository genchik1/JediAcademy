from django import forms
from .models import Сandidate, Answer, Question, Jedi
from django.forms.models import ModelMultipleChoiceField


class CustomSelectMultiple(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s: %s %s" %(obj.name, obj.short_description, obj.price)


class СandidateForm(forms.ModelForm):
    class Meta:
        model = Сandidate
        fields = ("name", "age", "habitat_planet", "email",)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("answer", "qestions",)



# class JediForm(forms.ModelForm):
#     select_candidate = CustomSelectMultiple(queryset=Сandidate.objects.all())
#     class Meta:
#         model = Jedi
#         fields = [
#             'select_candidate',
#         ]
#         widgets = {
#             'select_candidate': forms.CheckboxSelectMultiple(),
#         }



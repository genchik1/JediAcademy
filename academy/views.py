from django.shortcuts import render, get_object_or_404, redirect
from .models import Сandidate, Jedi, Answer, Question
from django.views.generic import ListView, DetailView
from django import forms
from django.views.generic.base import View
from .forms import СandidateForm, AnswerForm
from django.http import JsonResponse, HttpResponse


def candidateView(request):
    if request.method == "POST":
        form = СandidateForm(request.POST)
        if form.is_valid():
            form.save()
            candidate = Сandidate.objects.all().order_by('-id')[0]
            return redirect(candidate.get_absolute_url())
    else:
        form = СandidateForm()
    return render(request, 'candidate/form.html', {'form': form})


class CandidateDetailView(DetailView):
    model = Сandidate
    slug_field = "id"
    template_name = "candidate/candidate_detail.html"
    context_object_name = 'candidate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context


class JediView(ListView):
    model = Jedi
    queryset = Jedi.objects.all()
    template_name = "jedi/jedi_list.html"

    
class JediDetailView(DetailView):
    model = Jedi
    slug_field = "id"
    template_name = "jedi/jedi_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['candidate_list'] = Сandidate.objects.all()
        return context


def index(request):
    
    res = None

    context = {'types': res}

    return render(request, 'index.html', context)
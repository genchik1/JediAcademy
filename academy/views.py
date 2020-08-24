from django.shortcuts import render, get_object_or_404, redirect
from .models import Сandidate, Jedi
from django.views.generic import ListView, DetailView
from django import forms
from django.views.generic.base import View
from .forms import СandidateForm


def candidateView(request):
    if request.method == "POST":
        form = СandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = СandidateForm()
    return render(request, 'candidate/form.html', {'form': form})



class JediView(ListView):
    model = Jedi
    queryset = Jedi.objects.all()
    template_name = "jedi/jedi_list.html"

    
class JediDetailView(DetailView):
    model = Jedi
    slug_field = "id"
    template_name = "jedi/jedi_detail.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['candidate_list'] = Сandidate.objects.all()
        return context

def index(request):
    
    res = None

    context = {'types': res}

    return render(request, 'index.html', context)
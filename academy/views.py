from django.shortcuts import render, get_object_or_404, redirect
from .models import Сandidate, Jedi, Answer, Question, Choice, Grade
from django.views.generic import ListView, DetailView, CreateView
from django import forms
from django.http.request import QueryDict
from django.views.generic.base import View
from .forms import СandidateForm, AnswerForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse


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
        candidate = context['candidate']
        context['questions'] = Question.objects.all()
        context['padavan_status'] = Сandidate.objects.get(id=candidate.id).sensei
        return context


class AnswerQuestions(View):
    # model = Question
    # pk_field = "id"
    # template_name = "candidate/candidate_detail.html"
    # context_object_name = 'question'

    def myrequest(self, req):
        myreq = []
        for key, val in req.POST.dict().items():
            if key != 'csrfmiddlewaretoken':
                if key.startswith('answer'):
                    question = key.split('-')[1]
                    myreq.append({
                        'csrfmiddlewaretoken':req.POST.get('csrfmiddlewaretoken'),
                        'answer':val,
                        'qestions':question,
                    })
        return myreq

    def post(self, request, slug):
        my_dict = self.myrequest(request)
        candidate = Сandidate.objects.get(id=slug)
        for md in my_dict:
            form = AnswerForm(md)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.candidate = candidate
                myform.qestions = Question.objects.get(id=int(md['qestions']))
                myform.answer = Choice.objects.get(id=int(md['answer']))
                myform.save()
        return redirect(candidate.get_absolute_url())


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
        jedi = context['jedi']
        context['candidate_list'] = Сandidate.objects.filter(sensei__isnull=True)
        context['padavans'] = Сandidate.objects.filter(sensei=jedi)
        context['max_count_padavans'] = Grade.objects.get(title=jedi.grade).max_count_padavans
        context['count_padavans'] = Сandidate.objects.filter(sensei=jedi).count()
        return context

    def post(self, request, slug):
        jedi = Jedi.objects.get(id=slug)
        max_count_padavans = Grade.objects.get(title=jedi.grade).max_count_padavans
        count_padavans = Сandidate.objects.filter(sensei=jedi).count()
        if count_padavans < max_count_padavans:
            Сandidate.objects.update_or_create(
                id=request.POST.get("sensei"),
                defaults={'sensei':jedi}
            )
        return redirect(jedi.get_absolute_url())


def index(request):
    
    res = None

    context = {'types': res}

    return render(request, 'index.html', context)


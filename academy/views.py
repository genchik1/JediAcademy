from django.shortcuts import render, get_object_or_404, redirect
from .models import Сandidate, Jedi, Question, Choice, Grade, Answer
from django.views.generic import ListView, DetailView, CreateView
from django import forms
from django.http.request import QueryDict
from django.views.generic.base import View
from .forms import СandidateForm, AnswerForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.db.models import Q


class GradeCountPadavansView:
    """Жанры и года выхода фильмов"""
    def get_grade(self):
        return Grade.objects.all()

    def get_padavans(self):
        return Jedi.objects.order_by().values("count_padavans").distinct()


def candidateFormView(request):
    if request.method == "POST":
        form = СandidateForm(request.POST)
        if form.is_valid():
            form.save()
            candidate = Сandidate.objects.all().order_by('-id')[0]
            return redirect(candidate.get_absolute_url())
    else:
        form = СandidateForm()
    return render(request, 'candidate/form.html', {'form': form})


class CandidateView(ListView):
    model = Сandidate
    queryset = Сandidate.objects.all()
    template_name = "candidate/candidate_list.html"
    context_object_name = 'candidate_list'


class CandidateDetailView(DetailView):
    model = Сandidate
    slug_field = "id"
    template_name = "candidate/candidate_detail.html"
    context_object_name = 'candidate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        candidate = context['candidate']
        context['questions'] = Question.objects.all()
        context['padavan_status'] = Сandidate.objects.get(id=candidate.id).jedi
        return context


class AnswerQuestions(View):
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
        print (request)
        my_dict = self.myrequest(request)
        candidate = Сandidate.objects.get(id=slug)
        for md in my_dict:
            form = AnswerForm(md)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.candidate = candidate
                myform.qestions = Question.objects.get(id=int(md['qestions']))
                myform.ans = Choice.objects.get(id=int(md['answer']))
                myform.save()
                Сandidate.objects.update_or_create(
                    id=slug,
                    defaults={'answered_questions':True}
                )
        return redirect(candidate.get_absolute_url())


class JediView(GradeCountPadavansView, ListView):
    model = Jedi
    queryset = Jedi.objects.all()
    template_name = "jedi/jedi_list.html"

    
class JediDetailView(GradeCountPadavansView, DetailView):
    model = Jedi
    slug_field = "id"
    template_name = "jedi/jedi_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jedi = context['jedi']
        context['candidate_list'] = Сandidate.objects.filter(jedi__isnull=True)
        context['padavans'] = Сandidate.objects.filter(jedi=jedi)
        context['max_count_padavans'] = Grade.objects.get(title=jedi.grade.title).max_count_padavans
        context['count_padavans'] = jedi.count_padavans
        return context

    def post(self, request, slug):
        jedi = Jedi.objects.get(id=slug)
        max_count_padavans = Grade.objects.get(title=jedi.grade.title).max_count_padavans
        count_padavans = Сandidate.objects.filter(jedi=jedi).count()
        sent = False
        if count_padavans < max_count_padavans:

            # send_mail
            subject = 'Академия джедаев'
            message = f'Поздравляем! Вы зачислены в ученики {jedi.name}.'
            send_mail(subject, message, 'academy@jedi.com',[Сandidate.objects.get(id=request.POST.get("jedi")).email])
            sent = True

            Сandidate.objects.update_or_create(
                id=request.POST.get("jedi"),
                defaults={'jedi':jedi}
            )
            Jedi.objects.update_or_create(
                id=slug,
                defaults={'count_padavans':Jedi.objects.get(id=slug).count_padavans+1}
            )

        return redirect(jedi.get_absolute_url())


def index(request):
    res = None
    context = {'types': res, "candidate_list": Сandidate.objects.all()}
    return render(request, 'index.html', context)


class FilterGradeCountPadavansView(GradeCountPadavansView, ListView):
    """Фильтр"""
    template_name = "jedi/jedi_list.html"

    def get_queryset(self):
        queryset = Jedi.objects.filter(
            Q(grade__in=self.request.GET.getlist("grade")) |
            Q(count_padavans__in=self.request.GET.getlist("count_padavans"))
        )
        return queryset
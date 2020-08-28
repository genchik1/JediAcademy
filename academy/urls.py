from django.urls import path

from . import views

from django.views.generic import RedirectView


urlpatterns = [
    # task views
    path('candidate/form/', views.candidateFormView, name='candidate_form'),

    path('candidate/', views.CandidateView.as_view(), name='candidate'),
    path('candidate/<slug:slug>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
    path('candidate/<slug:slug>/question/', views.AnswerQuestions.as_view(), name='question'),

    path('jedi/', views.JediView.as_view(), name='jedis'),
    path("jedi/filter/", views.FilterGradeCountPadavansView.as_view(), name='filter'),
    path('jedi/<slug:slug>/', views.JediDetailView.as_view(), name='jedi_detail'),
    path('jedi/<slug:slug>/to_padavan/', views.JediDetailView.as_view(), name='to_padavan'),

    path('', views.index, name='index'),

    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico'), name='favicon'),
]

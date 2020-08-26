from django.urls import path

from . import views


urlpatterns = [
    # task views
    path('candidate/', views.candidateView, name='candidate'),
    path('candidate/<slug:slug>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
    path('candidate/<slug:slug>/question/', views.AnswerQuestions.as_view(), name='question'),
    path('jedi/', views.JediView.as_view(), name='jedis'),
    path('jedi/<slug:slug>/', views.JediDetailView.as_view(), name='jedi_detail'),
    path('jedi/<slug:slug>/to_padavan/', views.JediDetailView.as_view(), name='to_padavan'),
    path('', views.index, name='index'),
]

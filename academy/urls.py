from django.urls import path

from . import views


urlpatterns = [
    # task views
    path('candidate/', views.candidateView, name='candidate'),
    path('candidate/<slug:slug>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
    path('jedi/', views.JediView.as_view(), name='jedis'),
    path('jedi/<slug:slug>/', views.JediDetailView.as_view(), name='jedi_detail'),
    path('', views.index, name='index'),
]

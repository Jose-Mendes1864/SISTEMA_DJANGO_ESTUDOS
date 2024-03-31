
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('criar_pergunta/', views.criar, name='criar_pergunta'),
   path('criar_simulado/', views.criar_simulado, name='criar_simulado' )
]

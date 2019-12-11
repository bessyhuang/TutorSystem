from django.urls import path

from step1 import views

app_name = 'step1'

urlpatterns = [
    path('qu_step1/', views.qu_step1, name='qu_step1'),
]

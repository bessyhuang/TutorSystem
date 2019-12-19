from django.urls import path

from step2 import views

app_name = 'step2'

urlpatterns = [
    path('qu_step2/', views.qu_step2, name='qu_step2'),
]

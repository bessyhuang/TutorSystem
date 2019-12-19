from django.urls import path

from step3 import views

app_name = 'step3'

urlpatterns = [
    path('qu_step3/', views.qu_step3, name='qu_step3'),
]

from django.urls import path

from question import views

app_name = 'question'

urlpatterns = [
    path('qu_listSelect/', views.qu_listSelect, name='qu_listSelect'),
	path('qu_downloadData/', views.qu_downloadData, name='qu_downloadData'),
]

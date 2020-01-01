from django.urls import path

from upload import views

app_name = 'upload'

urlpatterns = [
    path('file_upload/', views.file_upload_view, name='file_upload'),
]

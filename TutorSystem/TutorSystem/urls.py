"""TutorSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from main import views
from account import views
from question import views
from upload.views import file_upload_view  ### 新增 ###

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	
	path('main/', include('main.urls', namespace='main')),
	path('account/', include('account.urls', namespace='account')),
	path('question/', include('question.urls', namespace='question')),
	path('step1/', include('step1.urls', namespace='step1')),

    path('file_upload/', file_upload_view, name='file_upload'),   ### 新增 ###

	#re_path('.*', views.main),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

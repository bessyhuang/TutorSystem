from django.shortcuts import render, redirect 
from upload.forms import *
from django.contrib import messages
# Create your views here.

#檔案會直接傳到media資料夾內，沒有另建其他資料夾
#https://www.geeksforgeeks.org/python-uploading-images-in-django/
#https://www.youtube.com/watch?v=AkkBc_d7OXk

def file_upload_view(request):
	if 'qu_title' and 'login_username' in request.session:
		qu_title = request.session['qu_title']
		login_username = request.session['login_username']
		print("file_upload_view: ", qu_title, login_username, "qu_step1")

		if request.method == 'POST': 
			form = File_UploadForm(request.POST, request.FILES)
			if form.is_valid(): 
				form.save()
				messages.add_message(request, messages.INFO, 'successfuly uploaded！')
				return redirect('/file_upload/') 
		else: 
			form = File_UploadForm() 
		return render(request, 'upload/html_for_upload.html', {'form': form}) 
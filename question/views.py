from django.shortcuts import render, redirect
from django.contrib import messages

from question.models import Qu_list

def qu_listSelect(request):
	
	### Test for session ###
	if 'login_username' in request.session:
		print(request.session['login_username'], "qu_listSelect")
	
	template = 'question/question_select.html'
	questionlist = Qu_list.objects.all()
	questionlist = Qu_list.objects.all().order_by('pub_date')
	#questionlist = Qu_list.objects.distinct('title')
	if request.method == 'GET':
		return render(request, template, {'questionlist': questionlist})
	
	### POST ###
	qu_title = request.POST['dropdown']
	request.session['qu_title'] = qu_title
	messages.success(request, '成功選取題目，請接著下載資料~')
	return redirect('question:qu_downloadData')
	
def qu_downloadData(request):
	template = 'question/question_downloadData.html'
	if 'qu_title' and 'login_username' in request.session:
		qu_title = request.session['qu_title']
		q_downloadData = Qu_list.objects.get(title=qu_title)
		
		### Test for session ###
		print(qu_title, request.session['login_username'], "qu_downloadData")
		
		### Query for models ###
		#questionlist = Qu_list.objects.all()
		#questionlist = Qu_list.objects.distinct('title')  --> learning later
		
		return render(request, template, {'q_downloadData': q_downloadData})
	else:
		return redirect('question:qu_listSelect')
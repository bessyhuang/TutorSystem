from django.shortcuts import render, redirect
from django.contrib import messages

from step1.models import Qu_step1

def qu_step1(request):
	
	### Test for session ###
	if 'qu_title' and 'login_username' in request.session:
		qu_title = request.session['qu_title']
		login_username = request.session['login_username']
		print(qu_title, login_username, "qu_step1")
	
	if 'user_input' in request.POST:
		user_input_text = request.POST.get('user_input')
		print("--- {} {} {} ---".format(qu_title, login_username, user_input_text))
		
		#qu_title = request.session['qu_title']
		detected_intent = "detected_intent"
		detected_intent_confidence = "detected_intent_confidence"
		chatbot_output_text = "chatbot_output_text"
		s1 = Qu_step1.objects.create(
			title=qu_title,
			username=login_username, 
			user_input_text=user_input_text, 
			detected_intent=detected_intent,
			detected_intent_confidence=detected_intent_confidence,
			chatbot_output_text=chatbot_output_text
		)
		s1.save()
		latest_QA = Qu_step1.objects.filter(username=login_username).order_by('timestamp')
		#s1_lastone = Qu_step1.objects.last()
		return render(request, 'step1/qu_step1.html', locals())	#, {'s1_lastone': s1_lastone}
		
	return render(request, 'step1/qu_step1.html')
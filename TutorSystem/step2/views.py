from django.shortcuts import render, redirect
from django.contrib import messages

from step2.models import Qu_step2

from google.api_core.exceptions import InvalidArgument
import dialogflow
from django.conf import settings
import os
import uuid

DFA_PROJECT_ID = 'django-statbot-shtmnf' #compute-wwsjtw
DFA_LANGUAGE = 'zh-TW'
DFA_SESSION_ID = uuid.uuid1()
DFA_JSON_DIR = os.path.join(settings.BASE_DIR, 'DialogflowAgent', 'Django-StatBot-35761ee24de2.json') #Compute-faea222692e7
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = DFA_JSON_DIR

def qu_step2(request):
	session_client = dialogflow.SessionsClient()
	DFA_session = session_client.session_path(DFA_PROJECT_ID, DFA_SESSION_ID)
	### Test for session ###
	if 'qu_title' and 'login_username' in request.session:
		qu_title = request.session['qu_title']
		login_username = request.session['login_username']
		print(qu_title, login_username, "qu_step2")
	
	if 'user_input' in request.POST:
		user_input_text = request.POST.get('user_input')
		print("--- {} {} {} ---".format(qu_title, login_username, user_input_text))
		#qu_title = request.session['qu_title']

		DFA_text_input = dialogflow.types.TextInput(text=user_input_text, language_code=DFA_LANGUAGE)
		DFA_query_input = dialogflow.types.QueryInput(text=DFA_text_input)

		### Get Response from Dialogflow API ###
		DFA_response = session_client.detect_intent(session=DFA_session, query_input=DFA_query_input)
		step2 = Qu_step2.objects.create(
			title=qu_title,
			username=login_username, 
			user_input_text=DFA_response.query_result.query_text, 
			detected_intent=DFA_response.query_result.intent.display_name,
			detected_intent_confidence=DFA_response.query_result.intent_detection_confidence,
			chatbot_output_text=DFA_response.query_result.fulfillment_text)
		step2.save()
		s2_lastone = Qu_step2.objects.filter(username=login_username).order_by('timestamp').last()
		
		print("---")
		print(s2_lastone)
		print("Query text:", DFA_response.query_result.query_text)
		print("Detected intent:", DFA_response.query_result.intent.display_name)
		print("Detected intent confidence:", DFA_response.query_result.intent_detection_confidence)
		print("Fulfillment text:", DFA_response.query_result.fulfillment_text)

		return render(request, 'step2/qu_step2.html', {'s2_lastone': s2_lastone})	#locals(), {'s1_lastone': s1_lastone}
		
	return render(request, 'step2/qu_step2.html', locals())
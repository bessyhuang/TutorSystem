from django.db import models

class Qu_step1(models.Model):
	title = models.CharField(max_length=128)
	username = models.CharField(max_length=128)
	user_input_text = models.CharField(max_length=100)
	detected_intent = models.CharField(max_length=255)
	detected_intent_confidence = models.CharField(max_length=255)
	chatbot_output_text = models.CharField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)

# 【Qu_step1】
	# title：題目名稱
	# username：使用者名稱
	# user_input_text：使用者輸入
	# detected_intent：使用者意圖
	# detected_intent_confidence：信心門檻
	# chatbot_output_text：機器人回覆
	# timestamp：作答結束之時間戳記
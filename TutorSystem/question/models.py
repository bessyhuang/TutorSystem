from django.db import models
from django.utils import timezone

class Qu_list(models.Model):
	title = models.CharField(max_length=128, unique=True)
	content = models.TextField()
	#當檔案透過管理者後台http://127.0.0.1:8000/admin上傳時, media/post_files資料夾會被自動建立。
	files = models.FileField(upload_to='files_download/') #, blank=True 可不上傳檔案
	pub_date = models.DateTimeField(default=timezone.now)
	
	class Meta:
		ordering = ('-pub_date',)
		
	def __str__(self):
		return self.title
		
# 【題目列表】
	# title：題目名稱
	# content：題目說明
	# files：管理員上傳檔案，供使用者下載
	# pub_date：建立題目的日期
from django.db import models
from django.utils import timezone

# Create your models here.
class File_Upload(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now) #auto_now_add=True

    #當檔案透過管理者後台http://127.0.0.1:8000/admin上傳時, media/post_files資料夾會被自動建立。
    #blank=True 可不上傳檔案; 
    upload_files = models.FileField(upload_to='files_upload/', blank=True) 

    class Meta:
        ordering = ('-upload_date',)

    def __str__(self):
        return self.title
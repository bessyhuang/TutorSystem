from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullName = models.CharField(max_length=128)
	# username：帳號 = 學號
	# password：密碼
	
    gender = models.CharField(choices=(("Male","男"), ("Female","女"),), max_length=32, default="女")
    university = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    
	#website = models.URLField(blank=True, null=True)
    #address = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.fullName + ' ( ' + self.username + ' )'
		
# 使用者【註冊】
	# fullName：真實姓名
	# username：帳號 = 學號
	# sex：性別	#sex = models.CharField(choices=(("male", u"男"), ("female", u"女")))
	# university：大學
	# department：科系
	# password：密碼
	# email：信箱
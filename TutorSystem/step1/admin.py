from django.contrib import admin
from step1.models import Qu_step1

class Qu_step1Admin(admin.ModelAdmin):
	list_display = ('title', 'username', 'user_input_text', 'timestamp')


admin.site.register(Qu_step1, Qu_step1Admin)
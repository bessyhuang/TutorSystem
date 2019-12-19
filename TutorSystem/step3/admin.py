from django.contrib import admin
from step3.models import Qu_step3

class Qu_step3Admin(admin.ModelAdmin):
	list_display = ('title', 'username', 'user_input_text', 'timestamp')


admin.site.register(Qu_step3, Qu_step3Admin)
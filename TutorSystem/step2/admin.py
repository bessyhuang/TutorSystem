from django.contrib import admin
from step2.models import Qu_step2

class Qu_step2Admin(admin.ModelAdmin):
	list_display = ('title', 'username', 'user_input_text', 'timestamp')


admin.site.register(Qu_step2, Qu_step2Admin)
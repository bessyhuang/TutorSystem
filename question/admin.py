from django.contrib import admin
from question.models import Qu_list

class Qu_listAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'files')


admin.site.register(Qu_list, Qu_listAdmin)
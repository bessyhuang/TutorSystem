from django.contrib import admin
from .models import File_Upload

# Register your models here.
class File_Upload_Admin(admin.ModelAdmin):
    list_display = ('title','slug','upload_date','upload_files')

admin.site.register(File_Upload, File_Upload_Admin)
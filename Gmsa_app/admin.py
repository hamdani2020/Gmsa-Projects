from django.contrib import admin
from . models import *

# Register your models here.
class HadithAdmin(admin.ModelAdmin):
    list_display = ["title","body","author","date"]

admin.site.register(Hadith,HadithAdmin)


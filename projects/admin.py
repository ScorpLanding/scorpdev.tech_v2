from django.contrib import admin
from .models import *

class ParserPhotoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ParserPhoto._meta.fields]

    class Meta():
        model = ParserPhoto

admin.site.register(ParserPhoto, ParserPhotoAdmin)
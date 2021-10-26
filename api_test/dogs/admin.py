from django.contrib import admin

from .models import DogImage


@admin.register(DogImage)
class NameAdmin(admin.ModelAdmin):
    list_display = ['id', 'url']

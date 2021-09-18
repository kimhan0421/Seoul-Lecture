from django.contrib import admin
from .models import LionClass


@admin.register(LionClass)
class LionClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_description', 'price', 'status']
    list_filter = ['title']
    search_fields = ['status']

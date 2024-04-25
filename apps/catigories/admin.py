from django.contrib import admin
from apps.catigories.models import Catigory
# Register your models here.

@admin.register(Catigory)
class CatigoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',),}
    
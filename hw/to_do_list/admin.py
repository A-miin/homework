from django.contrib import admin
from .models import Card

# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date']
    list_filter = [ 'description', 'status', 'date']
    search_fields = [ 'description', 'status', 'date']
    fields = [ 'description', 'status', 'date','more_description']
    readonly_fields = []


admin.site.register(Card, CardAdmin)
from django.contrib import admin
from .models import Card

# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'date']
    list_filter = [ 'name', 'status', 'date']
    search_fields = [ 'name', 'status', 'date']
    fields = [ 'name', 'status', 'date','description']
    readonly_fields = []


admin.site.register(Card, CardAdmin)
from django.urls import path

from .views import index, card_create

urlpatterns = [
    path('', index),  # URL для отображения списка статей
    path('new/', card_create)
]

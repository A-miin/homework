from django.urls import path

from .views import index, card_create, delete_card

urlpatterns = [
    path('', index),  # URL для отображения списка статей
    path('new/', card_create),
    path('delete/', delete_card ),
]

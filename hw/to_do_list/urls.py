from django.urls import path

from .views import index, card_create, delete_card

urlpatterns = [
    path('', index,name='list'),  # URL для отображения списка статей
    path('new/', card_create, name='new'),
    path('delete/', delete_card, name='delete' ),
]


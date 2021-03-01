from django.urls import path

from .views import index, card_create, delete_card, card_view

urlpatterns = [
    path('', index,name='list'),  # URL для отображения списка статей
    path('new/', card_create, name='new'),
    path('delete/<int:pk>', delete_card, name='delete' ),
    path('card/<int:pk>/', card_view, name='card-view')
]


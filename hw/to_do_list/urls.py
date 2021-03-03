from django.urls import path

from .views import (
                    index,
                    card_create,
                    card_delete,
                    card_view,
                    card_update,
                )

urlpatterns = [
    path('', index,name='list'),  # URL для отображения списка статей
    path('new/', card_create, name='new'),
    path('card/<int:pk>/delete', card_delete, name='card-delete' ),
    path('card/<int:pk>/', card_view, name='card-view'),
    path('card/<int:pk>/edit', card_update, name='card-update'),
]


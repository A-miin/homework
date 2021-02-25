from django.urls import path

from .views import index

urlpatterns = [
    path('', index),  # URL для отображения списка статей
]

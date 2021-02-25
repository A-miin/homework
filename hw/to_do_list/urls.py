from django.urls import path

from .views import index

urlpatterns = [
    path('', index_view),  # URL для отображения списка статей
]

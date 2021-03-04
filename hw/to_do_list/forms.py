from django import forms

from .models import Card


class CardForm(forms.ModelForm):
    """
    Форма для создания и редактирваония объектов статьи
    https://docs.djangoproject.com/en/3.1/ref/forms/
    """
    class Meta:
        model = Card
        fields = ('name', 'status', 'date', 'description')

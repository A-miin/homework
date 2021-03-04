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



def update_list():
    print('carddd')
    cards = []
    for card in Card.objects.all():
        cards.append((f'{card.id}',f'{card.name}'))
    return cards


class SimpleForm(forms.Form):
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=update_list(),
    )

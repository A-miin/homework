from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Card

# Create your views here.
def index(request):
    cards = Card.objects.all()
    context = {
        'cards':cards
    }
    return render(request, 'index.html', context)

def card_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'card_view.html', context={'card': card})


def card_create(request):
    """
    Представление для создания статьи
    """
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        return render(request, 'create_card.html')
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        name = request.POST.get("name")
        status = request.POST.get("status")
        date = request.POST.get("date")
        description = request.POST.get('description')
        if date=="":
            date=None
        if description=="":
            description=None
        card = Card.objects.create(
            name= name,
            status=status,
            date=date,
            description = description,
        )
        return redirect('card-view', pk=card.id)

def card_delete(request, pk):
    card = Card.objects.filter(id=pk)
    if request.method.GET:
        return render(request,'card_delete.html',card)

    return redirect('list')

def card_update(request, pk):
    card = get_object_or_404(Card, id=pk)
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        return render(request, 'card_update.html', {'card':card})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        name = request.POST.get("name")
        status = request.POST.get("status")
        date = request.POST.get("date")
        description = request.POST.get('description')
        if date=="":
            date=None
        if description=="":
            description=None
        card.name = name
        card.status = status
        card.date = date
        card.description = description
        card.save()
        return redirect('card-view', pk=card.id)

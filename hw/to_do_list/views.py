from django.shortcuts import render
from .models import Card

# Create your views here.
def index(request):
    cards = Card.objects.all()
    context = {
        'cards':cards
    }
    return render(request, 'index.html', context)

def card_create(request):
    """
    Представление для создания статьи
    """
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        return render(request, 'create_card.html')
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        description = request.POST.get("description")
        status = request.POST.get("status")
        date = request.POST.get("date")
        print(status)
        print(date)
        if date=="":
            date='Дата не указана'
        card = Card.objects.create(
            description= description,
            status=status,
            date=date
        )

        return render(request, 'index.html', {'cards':Card.objects.all()})

def delete_card(request):
    id = request.GET.get('id')
    Card.objects.filter(id=id).delete()
    return render(request, 'index.html', {'cards': Card.objects.all()})
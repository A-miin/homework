from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Card
from .forms import CardForm,SimpleForm,update_list

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
        form = CardForm()
        return render(request, 'create_card.html', context={'form': form})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        form = CardForm(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
        if form.is_valid():  # если форма валидна - создаётся статья и клиент редиректится
            card = Card.objects.create(
                name = form.cleaned_data.get('name'),
                status = form.cleaned_data.get('status'),
                date = form.cleaned_data.get('date'),
                description = form.cleaned_data.get('description')
            )
            return redirect('card-view',pk = card.id)  # Перенаправляем клиента на страницуу детального просмотра статьи
        return render(request, 'create_card.html',context={'form': form})  # если форма не валидна - отобразим форму с ошибками

def card_delete(request, pk):
    card = get_object_or_404(Card, id=pk)
    if request.method=='GET':
        return render(request, 'card_delete.html', {'card':card})
    elif request.method =='POST':
        if request.POST['action']=='Yes':
            card.delete()
        else:
            return redirect('card-view', pk=card.id)
    return redirect('list')

def card_update(request, pk):
    card = get_object_or_404(Card, id=pk)
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        form = CardForm(
            initial={  # создадим форму со стартоввыми данными полей, соответствующими данным полей статьи
                'name': card.name,
                'status':card.status,
                'date':card.date,
                'description': card.description
            })
        return render(request, 'card_update.html', {'card':card,'form':form})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        form = CardForm(data=request.POST)
        if form.is_valid():
            card.name = request.POST.get("name")
            card.status = request.POST.get("status")
            card.date = request.POST.get("date")
            card.description = request.POST.get('description')
            card.save()
            return redirect('card-view', pk=card.id)
        return render(request, 'card_update.html', {'card':card, 'form': form})

def bulk_delete(request):
    update_list()
    cards = Card.objects.all()
    if request.method=='GET':
        form = SimpleForm()
        return render(request, 'bulk delete.html', {'cards':cards, 'form':form})
    elif request.method=='POST':
        res = request.POST.getlist('favorite_colors')
        for pk in res:
            card = get_object_or_404(Card, id=int(pk))
            card.delete()
    # update_list()
    return redirect('list')
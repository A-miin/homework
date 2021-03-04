from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Card
from .forms import CardForm

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


"""
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
s
        return render(request, 'article_create.html', context={'form': form})
    elif request.method == "POST":  # Если метод запроса POST - создаём статью и редиректим клиента
        form = ArticleForm(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
        if form.is_valid():  # если форма валидна - создаётся статья и клиент редиректится
            article = Article.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=form.cleaned_data.get('author')
            )
            return redirect('article-view', pk=article.id)  # Перенаправляем клиента на страницуу детального просмотра статьи
        return render(request, 'article_create.html', context={'form': form})  # если форма не валидна - отобразим форму с ошибками

"""
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

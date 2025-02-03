from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Мой сайт'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


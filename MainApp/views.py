from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

person = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'middle_name': 'Петрович',
    'phone': '8-923-600-01-01',
    'email': 'vasya@mail.ru',
}

products = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    return render(request, 'index.html', person)


def about(request):
    return render(request, 'about.html', person)


def item(request, id: int):
    lstIds = [x['id'] for x in products]
    if id in lstIds:
        product = [x for x in products if x['id'] == id][0]
        return render(request, 'item.html', product)
    return render(request, 'error.html')


def items(request):
    return render(request, 'items.html', context={'products': products})

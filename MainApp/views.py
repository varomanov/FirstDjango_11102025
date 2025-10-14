from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item

# Create your views here.

person = {
    'first_name': 'Ivan',
    'last_name': 'Ivanov',
    'middle_name': 'Petrovich',
    'phone': '8-923-600-01-01',
    'email': 'vasya@mail.ru',
}

products = Item.objects.all()

def home(request):
    return render(request, 'index.html', person)


def about(request):
    return render(request, 'about.html', person)


def item(request, id: int):
    lstIds = [x.id for x in products]
    if id in lstIds:
        product = [x for x in products if x.id == id][0]
        return render(request, 'item.html', context={'name': product.name, 'count': product.count})
    return render(request, 'error.html')


def items(request):
    return render(request, 'items.html', context={'products': products})

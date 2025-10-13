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
    return render(request, 'index.html')


def about(request):
    text = f"""
    <div class='contact'>
        <p>Имя: {person.get('first_name')}</p>
        <p>Отчество: {person['middle_name']}</p>
        <p>Фамилия: {person['last_name']}</p>
        <p>телефон: {person['phone']}</p>
        <p>email: {person['email']}</p>
    </div>"""
    return HttpResponse(text)


def item(request, id: int):
    lstIds = [x['id'] for x in products]
    if id in lstIds:
        product = [x for x in products if x['id'] == id][0]
        text = f"""
        <p style='font-weight: bold;'>Product information:</p>
        <ul>
            <li>Name: {product['name']}</li>
            <li>Quantity: {product['quantity']}</li>
        </ul>
        <a href='/items'>Back to product list</a>
        """
        return HttpResponse(text)
    return HttpResponse('Товар не найден')


def items(request):
    list_items = ""
    for i in products:
        list_items += f'<li><a href="item/{i['id']}">{i}</a></li>'
    text = f"""
    <h2>All products</h2>
    <ol>{list_items}</ol>"""
    return HttpResponse(text)

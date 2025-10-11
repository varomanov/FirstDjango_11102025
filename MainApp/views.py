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


def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


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

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    header = "Данные пользователя"  # обычная переменная
    langs = ["Python", "Java", "C#"]  # список
    user = {"name": "Tom", "age": 23}  # словарь
    address = ("Абрикосовая", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
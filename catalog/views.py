from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def contact(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Вывод в консоль для отладки
        print(f"POST запрос получен: Имя={name}, Телефон={phone}, Сообщение={message}")

        # Возвращение ответа
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")

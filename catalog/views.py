from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactView(View):
    template_name = "catalog/contacts.html"

    def get(self, request):
        # Возвращаем страницу с формой через указанный шаблон
        return render(request, self.template_name)

    def post(self, request):
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Вывод в консоль для отладки
        print(f"POST запрос получен: Имя={name}, Телефон={phone}, Сообщение={message}")

        # Возвращение ответа
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'category', 'product_description', 'product_image', 'product_price', 'created_at', 'category']
    success_url = reverse_lazy('catalog:products_list')



class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'category', 'product_description', 'product_image', 'product_price', 'created_at']
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

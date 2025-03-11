from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.forms import inlineformset_factory

from catalog.forms import ProductForm, ParentForm, ProductModeratorForm
from catalog.models import Product, Parent, Category
from catalog.services import get_products_from_cache, get_products_by_category


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

    def get_queryset(self):
        return get_products_from_cache()


class ProductsByCategoryView(View):
    """Отображает список продуктов в указанной категории"""

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)  # Используем id вместо category_id
        products = get_products_by_category(category_id)

        return render(request, 'catalog/products_by_category.html', {'category': category, 'products': products})


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.request.user == self.object.owner:
    #         self.object.save()
    #         return self.object
    #     raise PermissionDenied


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    # fields = ['product_name', 'category', 'product_description', 'product_image', 'product_price', 'created_at', 'category']
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ['product_name', 'category', 'product_description', 'product_image', 'product_price', 'created_at']
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Parent, ParentForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied('Нет прав для редактирования')


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.has_perm('catalog.can_delete_product'):
            self.object.save()
            return self.object
        raise PermissionDenied

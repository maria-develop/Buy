from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from django.utils import timezone
from catalog.models import Product, Parent
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words_name = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
    forbidden_words_description = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                   'полиция', 'радар']
    class Meta:
        model = Product
        exclude = ("views_count", 'owner')
        # fields = "__all__"
        # fields = ['product_name', 'category', 'product_description', 'product_image', 'product_price', 'created_at', 'category']

    def clean_product_name(self):
        name = self.cleaned_data.get('product_name').lower()
        for word in self.forbidden_words_name:
            if word in name:
                raise forms.ValidationError("Имя продукта содержит запрещенное слово: {}".format(word))
        return name

    def clean_product_description(self):
        description = self.cleaned_data.get('product_description').lower()
        for word in self.forbidden_words_description:
            if word in description:
                raise forms.ValidationError("Описание содержит запрещенное слово: {}".format(word))
        return description

    def clean_product_price(self):
        price = self.cleaned_data.get('product_price')
        if price <= 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной или равной нулю.")
        return price


class ParentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"

    def clean_year_born(self):
        year_born = self.cleaned_data['year_born']
        current_year = timezone.now().year
        timedelta = current_year - year_born
        if timedelta >= 100:
            raise ValidationError('Неверная дата производства товара')
        return year_born

from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=150, verbose_name="Наименование категории"
    )
    category_description = models.CharField(
        max_length=200, verbose_name="Описание категории", blank=True, null=True
    )

    def __str__(self):
        return f"{self.category_name} {self.category_description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["category_name"]


class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
        null=True, blank=True,
    )
    product_description = models.TextField(
        verbose_name="Описание товара",
        null=True, blank=True,
    )
    product_image = models.ImageField(
        upload_to="catalog/images",
        verbose_name="Фотография",
        help_text="Загрузите фото товара",
    )
    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена товара",
        help_text="Введите цену товара",
        null=True, blank=True,
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        null=True, blank=True,
        help_text="Укажите дату создания",
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name="products",
        null=True, blank=True,
        related_query_name='products',
    )

    def __str__(self):
        return f"Наименование товара: {self.product_name}"
        # return (
        #     f"Наименование товара: {self.product_name}, "
        #     f"описание товара: {self.product_description}, "
        #     f"цена товара: {self.product_price}, "
        #     f"категория: {self.category}, "
        #     f"дата создания: {self.created_at}, дата изменения: {self.updated_at}"
        # )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = [
            "product_name",
            "product_description",
            "product_price",
            "category",
            "created_at",
            "updated_at",
        ]

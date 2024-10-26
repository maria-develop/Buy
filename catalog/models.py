from django.db import models

from users.models import User


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
    # UNPUBLISHED = 'unpublished'
    # PUBLISHED = 'published'
    # ARCHIVED = 'archived'
    #
    # STATUS_CHOICES = [
    #     (UNPUBLISHED, 'Не опубликовано'),
    #     (PUBLISHED, 'Опубликовано'),
    #     (ARCHIVED, 'В архиве'),
    # ]
    #
    # status = models.CharField(
    #     max_length=20,
    #     choices=STATUS_CHOICES,
    #     default=UNPUBLISHED,
    # )

    is_published = models.BooleanField(default=False)

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
        null=True, blank=True,
    )
    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена товара",
        help_text="Введите цену товара",
        null=True, blank=True,
    )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        null=True, blank=True,
        help_text="Укажите дату создания",
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Введите категорию',
        related_name="products",
        null=True,
        blank=True,
        related_query_name='products',
    )

    views_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        help_text='Укажите владельца продукта',
        blank=True, null=True,
        on_delete=models.SET_NULL,
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
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product'),
        ]


class Parent(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='parents',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Продукт',
    )

    product_name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
        null=True, blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Введите категорию',
        related_name="parents",
        null=True,
        blank=True,
        related_query_name='parents_products',
    )

    year_born = models.PositiveIntegerField(
        verbose_name='Год производства',
        help_text='Укажите год производства',
        default=0
    )

    class Meta:
        verbose_name = "Родительский товар"
        verbose_name_plural = "Родительские товары"
        ordering = [
            "product",
            "product_name",
            "category",
            "year_born",
        ]

    def __str__(self):
        return f"Наименование товара: {self.product_name}"

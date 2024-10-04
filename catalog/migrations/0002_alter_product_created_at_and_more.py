# Generated by Django 5.1.1 on 2024-10-03 18:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(
                blank=True,
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание товара"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(
                default=django.utils.timezone.now,
                help_text="Загрузите фото товара",
                upload_to="catalog/images",
                verbose_name="Фотография",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(
                blank=True,
                help_text="Введите наименование товара",
                max_length=100,
                null=True,
                verbose_name="Наименование товара",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Введите цену товара",
                max_digits=10,
                null=True,
                verbose_name="Цена товара",
            ),
        ),
    ]
# Generated by Django 4.2.2 on 2024-10-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото товара",
                null=True,
                upload_to="catalog/images",
                verbose_name="Фотография",
            ),
        ),
    ]

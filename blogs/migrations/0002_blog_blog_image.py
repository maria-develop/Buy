# Generated by Django 5.1.1 on 2024-10-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="blog_image",
            field=models.ImageField(
                blank=True,
                default="blogs/images/default.jpg",
                help_text="Загрузите фото",
                null=True,
                upload_to="blogs/images",
                verbose_name="Фотография",
            ),
        ),
    ]
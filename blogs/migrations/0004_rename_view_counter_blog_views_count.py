# Generated by Django 5.1.1 on 2024-10-05 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_remove_blog_views_count_blog_view_counter"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="view_counter",
            new_name="views_count",
        ),
    ]
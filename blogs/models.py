from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(
        max_length=150, verbose_name="Имя автора"
    )
    last_name = models.CharField(
        max_length=150, verbose_name="Фамилия автора"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "фамилия"
        verbose_name_plural = "фамилии"
        ordering = ["last_name"]


class Blog(models.Model):

    blog_name = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите наименование",
        null=True, blank=True,
    )
    blog_content = models.TextField(
        verbose_name="Содержимое",
        null=True, blank=True,
    )
    blog_image = models.ImageField(
        upload_to="blogs/images",
        verbose_name="Фотография",
        default="blogs/images/default.jpg",
        help_text="Загрузите фото",
        null=True, blank=True,
    )

    created_at = models.DateField(
        verbose_name="Дата создания",
        null=True, blank=True,
        help_text="Укажите дату создания",
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Признак публикации",
    )

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL,
        related_name="blog",
        null=True, blank=True,
        related_query_name='blogs',
    )

    views_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name="Slug",
        help_text="Автоматически генерируется из заголовка",
        null=True, blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заголовок: {self.blog_name}"

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = [
            "blog_name",
            "blog_content",
            "is_published",
            "author"
        ]

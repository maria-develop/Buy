from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy

from blogs.models import Blog


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.filter(is_published=True)

    def get_queryset(self):
        # Возвращаем только опубликованные статьи
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self):
        # Получаем объект блога
        blog = super().get_object()

        # Увеличиваем счетчик просмотров
        blog.views_count += 1
        blog.save(update_fields=['views_count'])  # Обновляем только поле views_count

        return blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['blog_name', 'blog_content', 'blog_image', 'is_published']
    success_url = reverse_lazy('blogs:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['blog_name', 'blog_content', 'blog_image', 'is_published']
    success_url = reverse_lazy('blogs:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog_list')

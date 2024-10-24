from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse

from blogs.models import Blog


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.filter(is_published=True)

    def get_queryset(self):
        # Возвращаем только опубликованные статьи
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        # Получаем объект блога
        self.object = super().get_object(queryset)

        # Увеличиваем счетчик просмотров
        self.object.views_count += 1
        self.object.save()  # Обновляем только поле views_count: (update_fields=['views_count'])

        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ['blog_name', 'blog_content', 'blog_image', 'is_published']
    success_url = reverse_lazy('blogs:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['blog_name', 'blog_content', 'blog_image', 'is_published']
    success_url = reverse_lazy('blogs:blog_list')

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog_list')

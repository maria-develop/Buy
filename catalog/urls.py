from django.urls import path, include
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactView, ContactView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductsByCategoryView


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("base/", ProductListView.as_view(), name='products_list'),
    path("catalog/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path("catalog/create/", ProductCreateView.as_view(), name='products_create'),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name='products_update'),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name='products_delete'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]

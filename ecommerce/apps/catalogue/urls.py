from django.urls import path

from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.product_all, name="store_home"),
    path("full", views.full_shop, name="full_shop"),
    path("product/<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
    path("search", views.search_results, name="search_results"),
]

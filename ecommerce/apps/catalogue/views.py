from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products= Product.objects.filter(title__contains=searched)
        return render(request, "search_result.html", {"searched": searched, "products": products})
    else:
        return render(request, "search_result.html", {})


def full_shop(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "catalogue/all_products.html", {"products": products})


def product_all(request):
    category = Category.objects.all()
    products = Product.objects.prefetch_related("product_image").filter(is_active=True).order_by('id')
    return render(request, "catalogue/index.html", {"products": products, "category": category})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category__slug__contains=category.slug)
    return render(request, "catalogue/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "catalogue/single.html", {"product": product})


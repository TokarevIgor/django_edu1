from django.shortcuts import get_object_or_404, render
from .models import ProductCategory, Product

MENU_LINKS = [
    {'view_name': 'main', 'name': 'домой'},
    {'view_name': 'products:index', 'name': 'продукты'},
    {'view_name': 'contact', 'name': 'контакты'}
]

def main(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Магазин',
        'menu_links': MENU_LINKS,
        'popular_products': Product.objects.filter(its_popular=True)
    })


def products(request, pk=None):
    if not pk:
        active_category = None
        products = Product.objects.all()
    else:
        active_category = get_object_or_404(ProductCategory, id=pk)
        products = Product.objects.filter(category=active_category)

    return render(request, 'mainapp/products.html', context={
        'title': 'Каталог',
        'menu_links': MENU_LINKS,
        'ls_category': ProductCategory.objects.all(),
        'products': products,
        'active_category': active_category
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })

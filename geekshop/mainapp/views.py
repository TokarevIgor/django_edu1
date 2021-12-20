from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket
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
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    basket = {
            'basket': [],
            'quantity': 0,
            'total': 0
        }
    if request.user.is_authenticated:
        basket_filter = Basket.objects.filter(user=request.user)
        basket = {
            'basket': basket_filter,
            'quantity': Basket.quantityBasket(basket_filter),
            'total': Basket.totalPriceBasket(basket_filter)
        }

    if pk is None:
        pk = 0

    if request.resolver_match.view_name == 'products:product' and pk != 0:
        product = get_object_or_404(Product, pk=pk)
        same_products = Product.objects.filter(category=product.category)[:3]

        content = {
            'title': product.name,
            'menu_links': MENU_LINKS,
            'ls_category': links_menu,
            'same_products': same_products,
            'product': product,
            'basket': basket,
        }

        return render(request, 'mainapp/products.html', content)

    else:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'menu_links': MENU_LINKS,
            'ls_category': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)   
    


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })

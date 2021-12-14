from django.shortcuts import render
import json
from .models import ProductCategory, Product

MENU_LINKS = [
    {'view_name': 'main', 'name': 'домой'},
    {'view_name': 'products:index', 'name': 'продукты'},
    {'view_name': 'contact', 'name': 'контакты'}
]

"""
def create_product(name, category, price, disc, img_path, its_new):    
    new_product = Product(name=name, category=ProductCategory.objects.get(name=category), price=price, img=img_path,
            its_new=its_new, discription=disc, short_discription=disc)
    new_product.save()
    pass


def create_category(name, disc, img_path, its_popular):
    new_cat = ProductCategory(name=name, discription=disc,
                    img=img_path, its_popular=its_popular)
    new_cat.save()
    pass

all_cat = ProductCategory.objects.all()
for cat in all_cat:
    ProductCategory.delete(cat)

all_product = Product.objects.all()
for prod in all_product:
    Product.delete(prod)


ls_category = [
    create_category('Стулья', 'Лучшие стулья в мире', 'category_images/product-1.jpg', True),
    create_category('Все для кухни',
                    'Удобные на кухне, применимы везде', 'category_images/product-2.jpg', True),
    create_category('Лампы', 'Светят классно', 'category_images/product-3.jpg', True),
    create_category('Вазы', 'Вазы для всех', 'category_images/product-4.jpg', True),
]


ls_products = [
    create_product('Белая лампа', 'Лампы', 212,
                   'Светит так что не видно ничего', 'products_images/product-11.jpg', True),
    create_product('Широкий стул', 'Стулья', 425,
                   'Расположитесь комфортно.\n Отличное качество материалов позволит вам это.\n Различные цвета', 'products_images/product-21.jpg', False),
    create_product('Черная настольная лампа', 'Лампы', 2588,
                   'С ней будет все темнее', 'products_images/product-31.jpg', False),
    create_product('Черная настенная лампа', 'Лампы', 25328,
                   'Повешать в душе и будет радость', 'products_images/product-41.jpg', True),
    create_product('Ступка', 'Все для кухни', 7832,
                   'Ступка, но не стопка', 'products_images/product-51.jpg', True),
    create_product('Походу ваза какая то', 'Вазы', 100,
                   'Можно положить в нее что-то', 'products_images/product-61.jpg', False)
]
"""

def main(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Магазин',
        'menu_links': MENU_LINKS,
        'popular_category': ProductCategory.objects.filter(its_popular=True)
    })


def products(request, pk=None):
    print(request.resolver_match.url_name)
    return render(request, 'mainapp/products.html', context={
        'title': 'Каталог',
        'menu_links': MENU_LINKS,
        'ls_category': ProductCategory.objects.all(),
        'products': Product.objects.all()
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })

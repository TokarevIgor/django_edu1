from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket
from .models import ProductCategory, Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import random

MENU_LINKS = [
    {'view_name': 'main', 'name': 'домой'},
    {'view_name': 'products:index', 'name': 'продукты'},
    {'view_name': 'contact', 'name': 'контакты'}
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Магазин',
        'menu_links': MENU_LINKS,
        'popular_products': Product.objects.filter(is_popular=True)
    })


def get_categories_menu():
    links_menu_category = ProductCategory.objects.filter(is_active=True)
    return links_menu_category


def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu_category = get_categories_menu()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(is_active=True,
                                           category__is_active=True).order_by('price')
            category = {'name': 'все', 'pk':0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'menu_links': MENU_LINKS,
            'links_menu_category': links_menu_category,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'menu_links': MENU_LINKS,
        'links_menu_category': links_menu_category,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })


def product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    content = {
        'title': product.name,
        'menu_links': MENU_LINKS,
        'links_menu_category': get_categories_menu(),
        'product': product,
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)

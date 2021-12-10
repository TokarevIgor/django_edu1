from django.shortcuts import render

menu_links = [
    {'view_name':'main', 'name': 'домой'},
    {'view_name':'products', 'name': 'продукты'},
    {'view_name':'contact', 'name': 'контакты'}
]


def main(request):
    return render(request, 'mainapp/index.html', context={
        'title' : 'Магазин',
        'menu_links': menu_links
    })


def products(request):
    return render(request, 'mainapp/products.html', context={
        'title' : 'Каталог',
        'menu_links': menu_links
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title' : 'Контакты',
        'menu_links': menu_links
    })

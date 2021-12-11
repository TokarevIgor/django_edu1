from django.shortcuts import render

menu_links = [
    {'view_name': 'main', 'name': 'домой'},
    {'view_name': 'products', 'name': 'продукты'},
    {'view_name': 'contact', 'name': 'контакты'}
]


def create_product(name, category, price, disc, img_path, its_new):
    return {
        'name': name,
        'category': category,
        'price': price,
        'disc': disc,
        'img_path': 'img/'+img_path,
        'it_new': its_new
    }


def create_category(name, disc, img_path, its_popular):
    return {
        'name': name,
        'disc': disc,
        'img_path': 'img/'+img_path,
        'its_popular': its_popular
    }


ls_products = [
    create_product('Белая лампа', 'Лампы', 212,
                   'Светит так что не видно ничего', 'product-11.jpg', True),
    create_product('Широкий стул', 'Стулья', 425,
                   'Расположитесь комфортно.\n Отличное качество материалов позволит вам это.\n Различные цвета', 'product-21.jpg', False),
    create_product('Черная настольная лампа', 'Лампы', 2588,
                   'С ней будет все темнее', 'product-31.jpg', False),
    create_product('Черная настенная лампа', 'Лампы', 25328,
                   'Повешать в душе и будет радость', 'product-41.jpg', True),
    create_product('Ступка', 'Все для кухни', 7832,
                   'Ступка, но не стопка', 'product-51.jpg', True),
    create_product('Походу ваза какая то', 'Вазы', 100,
                   'Можно положить в нее что-то', 'product-61.jpg', False)
]

ls_category = [
    create_category('Стулья', 'Лучшие стулья в мире', 'product-1.jpg', True),
    create_category('Все для кухни',
                    'Удобные на кухне, применимы везде', 'product-2.jpg', True),
    create_category('Лампы', 'Светят классно', 'product-3.jpg', True),
    create_category('Вазы', 'Вазы для всех', 'product-4.jpg', True),
]


def main(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Магазин',
        'menu_links': menu_links,
        'popular_category': [ct for ct in ls_category if ct['its_popular'] == True]
    })


def products(request):
    return render(request, 'mainapp/products.html', context={
        'title': 'Каталог',
        'menu_links': menu_links,
        'ls_category': ls_category,
        'products': ls_products
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': menu_links
    })

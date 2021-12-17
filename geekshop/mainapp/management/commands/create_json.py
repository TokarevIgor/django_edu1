import json
from django.core.management.base import BaseCommand

def create_product(name, category, price, disc, img_path, its_new, its_popular=False):    
    return {
        'name':name,
        'category':category,
        'price': price,
        'img': img_path,
        'its_new':its_new,
        'discription':disc,
        'short_discription':disc,
        "its_popular":its_popular
    }


def create_category(name, disc, img_path):
    return {
        'name':name,
        'discription':disc,
        'img': img_path
    }

ls_category = [
    create_category('Стулья', 'Лучшие стулья в мире', 'category_images/product-1.jpg'),
    create_category('Все для кухни',
                    'Удобные на кухне, применимы везде', 'category_images/product-2.jpg'),
    create_category('Лампы', 'Светят классно', 'category_images/product-3.jpg'),
    create_category('Вазы', 'Вазы для всех', 'category_images/product-4.jpg'),
]


ls_products = [
    create_product('Белая лампа', 'Лампы', 212,
                   'Светит так что не видно ничего', 'products_images/product-11.jpg', True, True),
    create_product('Широкий стул', 'Стулья', 425,
                   'Расположитесь комфортно.\n Отличное качество материалов позволит вам это.\n Различные цвета', 'products_images/product-21.jpg', False, True),
    create_product('Черная настольная лампа', 'Лампы', 2588,
                   'С ней будет все темнее', 'products_images/product-31.jpg', False),
    create_product('Черная настенная лампа', 'Лампы', 25328,
                   'Повешать в душе и будет радость', 'products_images/product-41.jpg', True),
    create_product('Ступка', 'Все для кухни', 7832,
                   'Ступка, но не стопка', 'products_images/product-51.jpg', True, True),
    create_product('Походу ваза какая то', 'Вазы', 100,
                   'Можно положить в нее что-то', 'products_images/product-61.jpg', False, True)
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('mainapp/json/categories.json', 'w+', encoding='utf-8') as f:
            json.dump(ls_category, f)

        with open('mainapp/json/products.json', 'w+', encoding='utf-8') as f:
            json.dump(ls_products, f)

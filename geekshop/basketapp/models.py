from django.db import models
from django.conf import settings
from mainapp.models import Product

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def quantityBasket(baskets:list):
        quantity = 0
        for basket in baskets:
            quantity += basket.quantity
        return quantity
    
    def totalPriceBasket(baskets:list):
        total = 0
        for basket in baskets:
            total += basket.product.price * basket.quantity
        return total
    

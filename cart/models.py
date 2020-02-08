from django.db import models
from pp.models import Pizza
from accounts.models import User


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # title + amount затем функция преобразует во вложенные списки
    pizza_list = models.CharField(max_length=400)

    total_cart_price = models.CharField(max_length=20, default=0)
    address = models.CharField(max_length=150, default='kek')

    created_at = models.DateTimeField(auto_now_add=True)

    def __iter__(self):
        for item in History.objects.all():
            yield item

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

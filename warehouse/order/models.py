from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models

from wBooks.models import Book


User = get_user_model


class Order(models.Model):
    UNDEFINED = 'UNDF'
    SENDED = 'SEND'
    SUBMITED = 'SBMT'
    PAID = 'PAID'
    SHIPPED = 'SHIP'
    DELIVERED = 'DLVR'

    oder_status = [
        (UNDEFINED, 'undefined'),
        (SENDED, 'sended'),
        (SUBMITED, 'submitted'),
        (PAID, 'paid'),
        (SHIPPED, 'shipped'),
        (DELIVERED, 'delivered'),
    ]

    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    suma = models.DecimalField('сумма заказа', max_digits=2, decimal_places=2, validators=[MinValueValidator(0, 'Значение не может быть отрицательным')])
    status = models.CharField(
        'статус заказа',
        max_length=4,
        choices=oder_status,
        default=UNDEFINED,
    )
    pub_date = models.DateTimeField()

    def __str__(self):
        return f'{self.username} {self.suma} {self.status}'

from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('first_name', 'last_name',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.CharField('Название', max_length=300, default='Noname', unique=True)
    price = models.DecimalField('цена', max_digits=10, decimal_places=2, default=0)
    rating = models.FloatField('рейтинг', blank=True, null=True, default=0)
    authors = models.ManyToManyField(Author, 'авторы')
    pubdate = models.DateField(blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

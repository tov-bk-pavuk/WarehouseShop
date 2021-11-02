from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField('Название', max_length=300)
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    rating = models.FloatField('рейтинг', blank=True, null=True)
    authors = models.CharField('авторы', max_length=300)
    pubdate = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = [['name', 'authors']]

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    name = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0, message='значение не может быть отрицательным')])

    def __str__(self):
        return self.name.name

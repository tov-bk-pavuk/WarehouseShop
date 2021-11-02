from random import choice, randrange, uniform

from django.core.management.base import BaseCommand

from faker import Faker

from catalog.models import Author, Book

fake = Faker()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, choices=range(50, 1000),
                            help=u'amount - от 10 до 1000')

    def handle(self, *args, **options):
        amount = options['amount']

        seq = [('0' + str(i)) for i in range(1, 10)]  # Блок генерации данных для дат
        seq += '11', '12'  # Месяцы
        seq_1 = seq + [str(i) for i in range(13, 29)]  # Числа месяца

        author = [Author(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birthday=f'{randrange(1920, 2020)}-{choice(seq)}-{choice(seq_1)}') for i in range(amount)]
        Author.objects.bulk_create(author)

        # publisher = [Publisher(name=fake.company()) for i in range(amount)]
        # Publisher.objects.bulk_create(publisher)

        # store = [Store(name=fake.company()) for i in range(amount)]
        # Store.objects.bulk_create(store)

        last = Author.objects.latest('pk')  # Блок для решения проблем с идентификатором
        last = last.id - amount + 1

        book = [Book(
            name=fake.catch_phrase(),
            price=round(uniform(150, 1500), 2),
            rating=round(uniform(1, 5), 1),
            pubdate=f'{randrange(1920, 2020)}-{choice(seq)}-{choice(seq_1)}',
            quantity=randrange(15)) for i in range(amount)]
        Book.objects.bulk_create(book)

        authors = Author.objects.all()
        length = len(authors)

        books = Book.objects.filter(pk__range=(last, amount + last - 1))
        for i in books:
            for k in [authors[randrange(length)] for i in range(randrange(1, 7))]:
                i.authors.add(k)

        if length > 25:
            length = 25

        # stores = Store.objects.filter(pk__range=(last, amount + last + 1))
        # for i in stores:
        #     for k in [books[randrange(len(books))] for i in range(randrange(9, length))]:
        #         i.books.add(k)

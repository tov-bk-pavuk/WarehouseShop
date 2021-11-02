from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, Author


class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'


def detail_book(request):
    pass


def authors_list(request):
    pass


def authors_detail(request):
    pass

from django.contrib import admin

from .models import Book, BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('rating',)
    list_display = ['name', 'rating', 'price', 'pubdate']
    fields = ('name', ('price', 'rating'), 'authors', 'pubdate')
    search_fields = ['name']
    # filter_horizontal = ['books']


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ['name', 'quantity']
    # fields = ('name', ('price', 'rating'), 'authors', 'pubdate')
    # search_fields = ['name']
    # filter_horizontal = ['authors']

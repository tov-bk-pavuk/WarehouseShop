from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ['username', 'suma', 'status']  # закрыть возможность изменения суммы заказа
    # fields = ('name', ('price', 'rating'), 'authors', 'pubdate')
    search_fields = ['username']
    # filter_horizontal = ['authors']

from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('detail_book/<int:id>', views.detail_book, name='detail_book'),
    path('authors_list', views.authors_list, name='authors_list'),
    path('authors_detail/<int:id>', views.authors_detail, name='authors_detail'),
]

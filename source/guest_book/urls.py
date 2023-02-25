from django.urls import path
from .views import book_list, book_create, BookDelete, book_update

urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/', book_create, name='book_create'),
    path('update/<int:pk>/', book_update, name='book_update'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='book_delete'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # category urls 
    path('category', category, name = 'category'),
    path('category/create', addCategory, name='addCategory'),
    path('category/<pk>/delete',deleteCategory, name= 'deleteCategory'),
    path('category/<pk>/edit', editCategory, name= 'editCategory'),
    
    # book urls 
    path('book', book_list, name = 'bookList'),
    path('book/create', addBook, name='addBook'),
    path('book/<pk>/delete',deleteBook, name= 'deleteBook'),
    path('book/<pk>/edit', editBook, name= 'editBook')
]



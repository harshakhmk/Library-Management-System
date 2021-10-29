from django.urls import reverse, path, include
from .views import *
urlpatterns = [
    path('',home,name='home'),# gets all the catalog of users books
    path('mybooks/',my_books,name='mybooks'),
    path('newbook/',newbook,name='newbook'),
]
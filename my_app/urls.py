from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *
urlpatterns = [
    path('cart/', cart, name='cart'),
    path('order/', order, name='order'),
    # path('main/', main, name='main'),
    path('main/', product_list, name='product_list'),
    path('main/<slug:slug>/', product_list, name='product_list_by_category'),
    path('main/<int:pk>/<slug:slug>/', product_detail, name='product_detail'),
]

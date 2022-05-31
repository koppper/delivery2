from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('', log_in, name='login'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('edit/', edit, name='edit'),
    path('logout', user_logout, name='logout'),
]

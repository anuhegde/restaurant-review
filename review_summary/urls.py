from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurants/', views.get_restaurants, name='get_restaurants'),
    re_path(r'^register/', views.register)
]
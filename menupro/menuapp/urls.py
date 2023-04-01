from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/<str:item_name>/', views.menu_detail, name='menu_detail' )
]
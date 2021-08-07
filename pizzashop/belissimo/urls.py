from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('menu', views.menu_page, name='menu'),
    path('contactus', views.contact_us, name='contactus'),
    path('services', views.services_page, name='services'),
    path('blog', views.blog_page, name='blog'),
    path('single', views.single_page, name='single'),
    path('about', views.about_page, name='about'),
    path('cart', views.cart_detail, name='cart'),
    path('contact', views.contact_page, name='contact'),
    path('sign/up', views.registration_page, name="registration"),
    path('sign/in', views.login_page, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
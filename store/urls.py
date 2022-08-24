from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('shop', views.shop , name="shop"),
    path('update_item/', views.updateItem, name="update_item"),
    path('logout_user', views.logout_user , name="logout" ),
    path('checkout/', views.checkout, name="checkout"),
    path('getvar/', views.getvar, name="getvar"),
    path('search/',views.searchProduct, name='search'),
    path('searchc/',views.searchProductByCat, name='searchc'),
    path('contact/',views.contact, name='contact'),
    path('test/',views.test, name='test'),
    path('register/',views.register_user, name='register'),
    path('login/',views.login_user, name='login'),
    path('profile/',views.profile, name='profile'),
    path('about/',views.about, name='about'),
    path('updateprofile/',views.updateprofile, name='updateprofile'),
    path('sefaresh/',views.sefaresh, name='sefaresh'),
    path('discount/',views.discount, name='discount'),
    path('gateway/',views.go_to_gateway_view, name='gateway'),
    path('cart/',views.cart, name='cart'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/finished.html"), name ='password_reset_complete'),
















]
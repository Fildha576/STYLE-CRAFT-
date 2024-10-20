from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('register',views.register),
    path('Login',views.doLogin),
    path('Logout',views.doLogout),
    path('t_register',views.t_register),
    path('view_users',views.view_users),
    path('view_approval',views.view_approval),
    path('appro/<int:id>',views.appro),
    path('reject/<int:id>',views.reject),
    path('view_tailor',views.view_tailor),
    path('product_add',views.product_add),


]

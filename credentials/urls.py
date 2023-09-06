from django.urls import path
from .import views


urlpatterns = [
    path('', views.index2, name='index2'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('newpage/', views.newpage, name='newpage'),
    path('form/', views.form_page, name='form_page'),

    ]
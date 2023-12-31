from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),

    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('invoice/', views.logout_user, name='invoice'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('signup/', views.signupPage, name = 'signup'),
    path('', views.loginPage, name = 'login'),
    path('logout/', views.logoutPage, name = 'logout'),
]
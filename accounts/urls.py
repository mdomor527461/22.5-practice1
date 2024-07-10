from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(),name = 'register'),
    path('login/',views.UserLoginView.as_view(),name = 'login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('profile/',views.UserUpdateView.as_view(),name = 'profile'),
]
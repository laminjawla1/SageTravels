from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# print(dir(auth_views.LoginView))
urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.MyLogoutView.as_view(), name="logout")
]
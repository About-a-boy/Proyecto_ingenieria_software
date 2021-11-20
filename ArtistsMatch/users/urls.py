"""Users urls module"""
from django.urls import path

from users import views


urlpatterns = [
    path(
        route='signup/',
        view=views.SignUp.as_view(),
        name="signup"
    ),
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name="login"
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        route='<str:username>/',
        view=views.ProfileView.as_view(),
        name="profile"
    ),
]

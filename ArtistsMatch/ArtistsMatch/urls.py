"""ArtistsMatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
import users.views as UsersViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='', 
        view=UsersViews.Index.as_view(),
        name="index"
    ),
    path(
        route='signup/',
        view=UsersViews.SignUp.as_view(),
        name="signup"
    ),
    path(
        route='login/',
        view=UsersViews.LoginView.as_view(),
        name="login"
    ),
    path(
        route='logout/',
        view=UsersViews.LogoutView.as_view(),
        name="logout"
    ),
    path(
        route='<str:username>/',
        view=UsersViews.ProfileView.as_view(),
        name="profile"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

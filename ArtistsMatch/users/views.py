"""Auth views"""
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import FormView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import SignUpForm


class Index(TemplateView):
    """Home view, the place where if no logged in 
    they will be looking at"""
    template_name = "index.html"


class SignUp(FormView):
    """Manage user sign up"""
    template_name = "registro.html"
    form_class = SignUpForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        """Form saving"""
        form.save()
        return super().form_valid(form)


class LogoutView(LogoutView):
    """Manage logout logic"""
    template_name = "index.html"


class LoginView(LoginView):
    """Managging login view"""
    template_name = "inicio_sesion.html"

    def get_success_url(self) -> str:
        succes_url = reverse('profile', kwargs={ "username": self.request.user.username })
        return succes_url


class ProfileView(LoginRequiredMixin, DetailView):
    """Profile Detail view"""
    template_name = "profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()
    context_object_name = 'user'
    

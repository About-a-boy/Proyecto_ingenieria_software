"""Auth views"""
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import FormView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import SignUpForm
from hits.models import Collaboration, collaboration


class Index(TemplateView):
    """Home view, the place where if no logged in 
    they will be looking at"""
    template_name = "index.html"


class SignUp(FormView):
    """Manage user sign up"""
    template_name = "registro.html"
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Form saving"""
        form.save()
        return super().form_valid(form)


class LogoutView(LogoutView):
    """Manage logout logic"""
    template_name = "index.html"


class LoginView(LoginView):
    """Managging login view"""
    template_name = "sing-in.html"

    def get_success_url(self):
        username = self.request.user.username
        success_url = reverse('users:profile', kwargs={ "username": username })
        return success_url


class ProfileView(LoginRequiredMixin, DetailView):
    """Profile Detail view"""
    template_name = "users/paginas_artistas.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        collaborations = Collaboration.objects.filter(artist=self.request.user.artist)
        context_data["hits"] = [collaboration.hit for collaboration in collaborations]
        return context_data
    

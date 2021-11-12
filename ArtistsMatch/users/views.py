"""Auth views"""
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy

from users.forms import SignUpForm


class Index(TemplateView):
    """Home view, the place where if no logged in 
    they will be looking at"""
    template_name = "index.html"


class SignUp(FormView):
    """Manage user sign up"""
    template_name = "registro.html"
    form_class = SignUpForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        """Form saving"""
        form.save()
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = "profile.html"

"""Auth views"""
from django.views.generic.base import TemplateView


class Index(TemplateView):
    """Home view, the place where if no logged in 
    they will be looking at"""
    template_name = "index.html"
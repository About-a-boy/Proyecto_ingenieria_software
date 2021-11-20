"""Views module"""
from django.views.generic import CreateView

from hits.forms import CreateHitForm

class CreateHitView(CreateView):
    """Create Hit View"""
    template_name = "crear_hit.html"
    form_class = CreateHitForm
    

"""Views module"""
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

from hits.forms import CreateCollaborationForm, CreateHitForm
from hits.models import Hit
from hits.models.collaboration import Collaboration

@login_required
def createHitView(request):
    request_post_modified = request.POST.copy()
    request_post_modified["collaborators"] = request.user.pk
    form = CreateHitForm(request_post_modified or None, request.FILES or None)
    context = {
        'form': form,
    }

    if request.is_ajax():
        if form.is_valid():
            hit = form.save()
            return JsonResponse({ 'hit': hit.pk })

    if request.method == 'POST' and not request.is_ajax():
        if form.is_valid():
            hit = form.save()
            url = reverse("hits:hit", kwargs={"pk": hit.pk})
            return redirect(url)

    
    return render(request, 'hits/crear_hit.html', context)


class HitDetailView(DetailView):
    """Hit Detail View class"""
    template_name = "hits/hit.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    queryset = Hit.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        collaboration = Collaboration.objects.filter(hit=self.object).first()
        context_data["creator"] = collaboration.artist.user.username

        return context_data


@login_required
def createCollaborationView(request, pk):
    local_request_post = request.POST.copy()
    local_request_post["artist"] = request.user.artist
    local_request_post["hit"] = pk
    form = CreateCollaborationForm(local_request_post or None, request.FILES or None)

    if request.is_ajax():
        if form.is_valid():
            collaboration = form.save()
            return JsonResponse({ "collaboration": collaboration.pk })
    
    if request.method in ["POST"] and not request.is_ajax():
        if form.is_valid():
            collaboration = form.save()
            url = reverse("hits:hit", kwargs={"pk": pk})
            return redirect(url)

    return render(request, "hits/collaboration.html", {
        "pk": pk,
        "form": form
    })


class Feed(ListView):
    """Feed class"""
    template_name = "hits/feed.html"
    queryset = Hit.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        collaboration = Collaboration.objects.filter(artist=self.request.user.artist).order_by("created")
        try:
            context_data["hit"] = collaboration[0].hit
        except IndexError:
            context_data["hit"] = ""
        context_data["hits"] = Hit.objects.all().order_by("created")
        return context_data

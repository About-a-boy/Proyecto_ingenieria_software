"""Views module"""
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from hits.forms import CreateCollaborationForm, CreateHitForm
from hits.models import Hit

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

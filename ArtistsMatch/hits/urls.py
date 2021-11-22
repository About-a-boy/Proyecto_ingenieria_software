"""Hits urls module"""
from django.urls import path

import hits.views as views

urlpatterns = [
    path(
        '',
        view=views.Feed.as_view(),
        name="feed"
    ),
    path(
        'new/',
        view=views.createHitView,
        name="new"
    ),
    path(
        "<int:pk>/collaborate/",
        view=views.createCollaborationView,
        name="collaborate"
    ),
    path(
        "<int:pk>/",
        view=views.HitDetailView.as_view(),
        name="hit"
    ),
]

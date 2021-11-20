"""Hits urls module"""
from django.urls import path

import hits.views as views

urlpatterns = [
    path(
        'new/',
        view=views.CreateHitView.as_view(),
        name="new"
    )
]
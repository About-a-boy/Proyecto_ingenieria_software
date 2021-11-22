"""Hits forms module"""
from django.contrib.auth.models import User
from django import forms

from hits.models import Hit
from hits.models.collaboration import Collaboration

class HitModelForm(forms.ModelForm):
    class Meta:
        model = Hit
        fields = '__all__'

class CreateHitForm(forms.ModelForm):
    """Create Hit Form"""
    hit = forms.IntegerField(required=False)
    collaborators = forms.IntegerField()

    def clean_collaborators(self):
        pk = self.data["collaborators"]
        user = User.objects.get(pk=pk)

        return user.artist

    def save(self):
        collaborators = self.cleaned_data["collaborators"]

        # import ipdb; ipdb.set_trace()

        if self.cleaned_data["hit"] is not None:
            pk = self.cleaned_data["hit"]
            hit = Hit.objects.get(pk=pk)

            if self.cleaned_data["song"] is not None:
                song = self.cleaned_data["song"]
                hit.song = song

            if self.cleaned_data["cover"] is not None:
                cover = self.cleaned_data["cover"]
                hit.cover = cover

            if self.cleaned_data["title"] is not None:
                title = self.cleaned_data["title"]
                hit.title = title

            if self.cleaned_data["description"] is not None:
                description = self.cleaned_data["description"]
                hit.description = description
        else:
            if self.cleaned_data["song"] is not None:
                    song = self.cleaned_data["song"]
                    hit = Hit.objects.create(song=song)

            if self.cleaned_data["cover"] is not None:
                cover = self.cleaned_data["cover"]
                hit = Hit.objects.create(cover=cover)

            hit.collaborators.add(collaborators)

        hit.save()

        return hit

    class Meta:
        model = Hit
        fields = '__all__'


class CreateCollaborationForm(forms.ModelForm):
    """Create collaboration form"""
    collaboration = forms.IntegerField(required=False)

    class Meta:
        model = Collaboration
        fields = ("song", "message")
    
    def save(self):
        if not self.cleaned_data["message"]:
            hit = Hit.objects.get(pk=self.data["hit"])
            collaboration = Collaboration.objects.create(
                artist=self.data["artist"],
                hit=hit
            )
            collaboration.save()
        else:
            collaboration = Collaboration.objects.filter(
                pk=self.data["collaboration"]
            ).update(message=self.cleaned_data["message"])

        return collaboration

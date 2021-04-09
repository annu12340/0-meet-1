from django import forms

from.models import Idea_Post

class Idea_PostModelForm(forms.ModelForm):
    class Meta:
        model=Idea_Post
        fields = ['title','description']

from django.shortcuts import render, redirect
from .models import Idea_Post
from .forms import Idea_PostModelForm

def home(request):
	homePost = Idea_Post.objects.all()
	return render(request, 'post_ideas/home.html', {"homePost":homePost})

def addPost(request):
    form=Idea_PostModelForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.createdby_id=request.user.pk
        instance.save()
        return redirect("home")
    return render(request, "post_ideas/addPost.html", {"form": form})



from django.shortcuts import render, redirect
from .models import PostIdeaModel
from .forms import Idea_PostModelForm

def home(request):
	AllPosts = PostIdeaModel.objects.all().order_by('-id')
	return render(request, 'post/home.html', {"AllPosts":AllPosts})

def addPost(request):
    form=Idea_PostModelForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.createdby_id=request.user.pk
        instance.save()
        return redirect("home")
    return render(request, "post/addPost.html", {"form": form})

def ParticularPost(request,id):
    print("inside particular q id is", id)
    individual_post = PostIdeaModel.objects.get(id=id)
    return render(request,'post/ParticularPost.html',{ "post":individual_post})
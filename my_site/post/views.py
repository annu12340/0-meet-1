
from django.shortcuts import render, redirect
from .models import PostIdeaModel,EventsIdeaModel
from .forms import Idea_PostModelForm

def home(request):
    AllPosts = PostIdeaModel.objects.all().order_by('-id')
    AllEvents = EventsIdeaModel.objects.all().order_by('-id')
    return render(request, 'post/home.html', {"AllPosts": AllPosts, "AllEvents": AllEvents })

def addPost(request):
    form=Idea_PostModelForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.createdby_id=request.user.pk
        instance.save()
        return redirect("home")
    return render(request, "post/addPost.html", {"form": form})

def addEvents(request):
    if(request.POST):
        ename=request.POST.get('ename')
        etype= request.POST.get('typeofevent')
        edate= request.POST.get('dateofevent')
        eplace = request.POST.get('place')
        edescrip= request.POST.get('description')
        elink = request.POST.get('linktoevent')
        E = EventsIdeaModel(EventName=ename, EventDate=edate, EventType=etype, EventPlace=eplace, Description=edescrip, EventLink=elink)
        E.save()

    return render(request, "post/addEvents.html")

def ParticularPost(request,id):
    print("inside particular q id is", id)
    individual_post = PostIdeaModel.objects.get(id=id)
    return render(request,'post/ParticularPost.html', { "post":individual_post})
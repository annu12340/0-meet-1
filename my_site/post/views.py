
from django.shortcuts import render, redirect
from .models import PostIdeaModel,EventsIdeaModel
from .forms import Idea_PostModelForm

def home(request):
    AllPosts = PostIdeaModel.objects.all().order_by('-id')
    AllEvents = EventsIdeaModel.objects.all().order_by('-id')
    return render(request, 'post/home.html', {"AllPosts": AllPosts, "AllEvents": AllEvents })

def addPost(request):
    if (request.POST):
        ptitle = request.POST.get('title')
        pdescrip = request.POST.get('description')
        pimg = request.POST.get('img')
        progress = request.POST.get('progress')
        teamsize = request.POST.get('teamsize')
        invsize = request.POST.get('invsize')
        fund = request.POST.get('fund')
        finance = request.POST.get('finance')
        patent = request.POST.get('patent')
        history = request.POST.get('history')
        P = PostIdeaModel(Title=ptitle, Description=pdescrip, Img=pimg, Progress=progress, CurrentTeamSize=teamsize, InvestorSize=invsize, FundingAmount=fund, FinancialStatus=finance, PatentDetails=patent, History=history,createdby_id = request.user.pk,createdby_image=request.user.last_name )
        P.save()

    return render(request, "post/addPost.html")

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
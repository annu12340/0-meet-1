
from django.shortcuts import render, redirect
from .models import PostIdeaModel,EventsIdeaModel, Notification
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
    if (request.POST):
        sendto_id = request.POST.get('sendto_id')
        message = request.POST.get('message')
        n = Notification(sendfrom_id=request.user.pk,sendfrom_name=request.user.first_name,sendfrom_img=request.user.last_name,sendto_id=sendto_id,message=message)
        n.save()
    print("inside particular q id is", id)
    individual_post = PostIdeaModel.objects.get(id=id)
    status=Notification.objects.filter(sendfrom_id=request.user.pk)
    print(status)
    if status:
        finalstatus=Notification.objects.filter(sendfrom_id=request.user.pk).filter(status='Accepted')
        if finalstatus:
            msg='Make payment'
            button_class = ''
        else:
            msg='Request is pending'
            button_class='btn btn-secondary btn-sm disabled'
    else:
        msg='Connect with founders'
        button_class='btn btn-dark btn-sm'

    return render(request,'post/ParticularPost.html', { "post":individual_post,"msg":msg,"button_class":button_class})


def network(request):
    if (request.POST):
        n = Notification.objects.filter(sendto_id=request.user.pk).filter(sendfrom_id=3)[0]
        n.status="Accepted"
        n.save()
    notification = Notification.objects.filter(sendto_id=request.user.pk).order_by('-id')
    return render(request, 'post/notification.html', {"notification": notification })

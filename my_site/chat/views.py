from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
from .models import messageStore
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model


def view_all_users_for_chat(request):
	user = get_user_model()
	alluser = user.objects.all()
	return render(request, 'chat/welcome.html', {'customer':alluser})


@login_required
def index(request):
	current_user = request.user.username
	users = User.objects.all().exclude(username=current_user)
	context = {'users':users}
	return render(request,'chat/welcome.html', context)


@login_required
def inbox(request,reciever_id=1):
	if request.method == 'POST':
		reciever_ins = User.objects.get(id=reciever_id)
		obj = messageStore.manager.create(msg=request.POST['msg'],sender=request.user,reciever=reciever_ins)
		
		msg =  messageStore.manager.get_msg(request.user.id,reciever_id)
		context={'msg':msg,'reciever_id':reciever_id}
		return render(request,'chat/inbox.html',context)
	else :
		msg =  messageStore.manager.get_msg(request.user.id,reciever_id)
		alluser = get_user_model().objects.all()
		context={'msg':msg,'reciever_id':reciever_id,'customer':alluser}

		return render(request,'chat/inbox.html',context)
	

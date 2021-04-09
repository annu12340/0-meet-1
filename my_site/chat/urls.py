from django.urls import path,include
from .views import *
urlpatterns = [
path('home1/', index, name='chatroom_home'),

path('abc/', abc ),


path('inbox/<int:reciever_id>',inbox,name='inbox'),
#path('inbox_re/<int:reciever_id>',inbox_re,name='inbox_re'),

]

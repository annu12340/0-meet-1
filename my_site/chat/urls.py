from django.urls import path,include
from .views import *
urlpatterns = [

path('all/', view_all_users_for_chat, name='view_all_users_for_chat' ),


path('inbox/<int:reciever_id>',inbox,name='inbox'),


]

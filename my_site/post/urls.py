from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('<int:id>/', views.ParticularPost, name='ParticularPost'),
    path('addIdeas/', views.addPost, name ="addIdeas"),
    path('addEvents/', views.addEvents, name="addEvents"),
    path('mynetwork/', views.network, name="mynetwork"),
    path('accept/<int:id>', views.accept, name="accept"),
    path('ignore/<int:id>', views.ignore, name="ignore"),
]
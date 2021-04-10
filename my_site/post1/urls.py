from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('addIdeas/', views.addPost, name ="addIdeas"),
    path('addEvents/', views.addEvents, name="addEvents"),

    path('<int:id>/', views.ParticularPost, name='ParticularPost'),
]


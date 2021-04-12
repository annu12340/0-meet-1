
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('authenticate.urls')),
    path('post/', include('post.urls')),
    path('', include('post.urls')), # added it here just to deploy
    path('chatroom/', include('chat.urls')),
]

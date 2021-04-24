from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static
from mysite.settings import  STATIC_ROOT, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('authenticate.urls')),
    path('post/', include('post.urls')),
    path('', include('authenticate.urls')), # added it here just to deploy
    path('chatroom/', include('chat.urls')),
    # ok i edit
    path('', include('pay.urls')),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+ static(STATIC_URL, document_root=STATIC_ROOT)



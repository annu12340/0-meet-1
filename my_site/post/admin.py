from django.contrib import admin
from .models import PostIdeaModel, EventsIdeaModel, Notification

# Register your models here.
# reg to admin panel

admin.site.register(PostIdeaModel)
admin.site.register(EventsIdeaModel)
admin.site.register(Notification)
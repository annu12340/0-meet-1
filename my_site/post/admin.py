from django.contrib import admin
from .models import PostIdeaModel
from .models import EventsIdeaModel

# Register your models here.
# reg to admin panel

admin.site.register(PostIdeaModel)
admin.site.register(EventsIdeaModel)
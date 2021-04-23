from django.contrib import admin
from .models import PostIdeaModel
from .models import EventsIdeaModel

# Register your models here.
# reg to admin panel
class eventAdmin(admin.ModelAdmin):
    list_display = ('EventName', 'EventDate', 'EventType')
    list_filter = ('EventDate',)


class postAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Description', 'Progress')
    list_filter = ('Title',)


admin.site.register(PostIdeaModel,postAdmin)
admin.site.register(EventsIdeaModel,eventAdmin)
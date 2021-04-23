from django.contrib import admin
from .models import messageStore
# Register your models here.

class messageAdmin(admin.ModelAdmin):
    list_display = ('msg','sender','reciever')

admin.site.register(messageStore,messageAdmin)
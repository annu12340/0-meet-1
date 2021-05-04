from django.db import models
from django.contrib.auth.models import User

class PostIdeaModel(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Img = models.CharField(max_length=200)
    ExceptedPrice = models.IntegerField()

    Progress = models.IntegerField()
    CurrentTeamSize = models.IntegerField()
    InvestorSize = models.IntegerField()

    FundingAmount = models.IntegerField()
    FinancialStatus = models.CharField(max_length=200)
    PatentDetails = models.CharField(max_length=200)
    History = models.CharField(max_length=200)

    createdby_id= models.IntegerField()
    createdby_name= models.CharField(max_length=200)
    createdby_image = models.CharField(max_length=200)


    def __str__(self):
        return self.Title


class EventsIdeaModel(models.Model):
    EventName = models.CharField(max_length=200)
    EventDate = models.DateField(null=True)
    EventType = models.CharField(max_length=200)
    EventPlace = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    EventLink = models.CharField(max_length=200)
    def __str__(self):
        return self.EventName


class Notification(models.Model):
        sendfrom_id= models.IntegerField()
        sendfrom_name = models.CharField(max_length=200)
        sendfrom_img = models.CharField(max_length=200)
        sendto_id= models.IntegerField()
        sendto_name = models.CharField(max_length=200)
        status = models.CharField(max_length=200, default="Pending")
        message= models.CharField(max_length=200)

        def __str__(self):
            return self.sendfrom_name+' to '+str(self.sendto_id)
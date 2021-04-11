from django.db import models


class PostIdeaModel(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Img = models.CharField(max_length=200)

    Progress = models.IntegerField()
    CurrentTeamSize = models.IntegerField()
    InvestorSize = models.IntegerField()

    FundingAmount = models.IntegerField()
    FinancialStatus = models.CharField(max_length=200)
    PatentDetails = models.IntegerField()
    History = models.CharField(max_length=200)
    createdby_id = models.IntegerField()

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

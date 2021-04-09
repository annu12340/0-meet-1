from django.db import models


class PostIdeaModel(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Img = models.CharField(max_length=200)

    Progress= models.IntegerField()
    CurrentTeamSize= models.IntegerField()
    InvestorSize= models.IntegerField()

    FundingAmount = models.IntegerField()
    FinancialStatus = models.CharField(max_length=200)
    PatentDetails= models.IntegerField()
    History=models.CharField(max_length=200)
    createdby_id = models.IntegerField()



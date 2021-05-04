from django import forms

from .models import PostIdeaModel


class Idea_PostModelForm(forms.ModelForm):
    class Meta:
        model = PostIdeaModel
        fields = ['Title', 'Description', 'Img', 'Progress', 'CurrentTeamSize', 'InvestorSize', 'FundingAmount',
                  'FinancialStatus', 'PatentDetails', 'History', 'ExceptedPrice']
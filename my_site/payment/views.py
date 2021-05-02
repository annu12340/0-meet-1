from django.shortcuts import render

# Create your views here.
# import resource

import stripe
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
stripe.api_key= settings.STRIPE_SECRET_KEY


from django.views.generic import View

# class Home(View):
#    template_name = 'templates/home.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key']=settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method=='POST':
        charge = stripe.Charge.create(
            amount=120,
            currency='INR',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
    return render(request, 'charge.html', {})
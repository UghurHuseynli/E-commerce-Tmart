from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import ContactModel
from .forms import ContactModelForm

# Create your views here.

def index(requests):
    return render(requests, 'index.html')

def about(requests):
    return render(requests, 'about.html')

class ContactView(SuccessMessageMixin, CreateView):
    model = ContactModel
    form_class = ContactModelForm
    template_name = 'contact.html'
    success_message = 'Your message has been taken into account, we will contact you soon.'
def team(requests):
    return render(requests, 'team.html')
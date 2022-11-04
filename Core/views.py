from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import CreateView, View
from django.contrib.messages.views import SuccessMessageMixin
from .models import ContactModel
from .forms import ContactModelForm
from Product.models import ProductModel, CategoryModel

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'products': ProductModel.objects.all(),
            'categories': CategoryModel.objects.all()
        }
        return render(request, 'index.html', context=context)



def about(requests):
    return render(requests, 'about.html')

class ContactView(SuccessMessageMixin, CreateView):
    model = ContactModel
    form_class = ContactModelForm
    template_name = 'contact.html'
    success_message = 'Your message has been taken into account, we will contact you soon.'

    
def team(requests):
    return render(requests, 'team.html')
from django.shortcuts import render
from django.views.generic import CreateView, View, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from .models import ContactModel, TeamModel
from .forms import ContactModelForm
from Product.models import ProductModel, CategoryModel, BrandModel, ProductVersionModel
from Blog.models import BlogModel

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'blogs': BlogModel.objects.order_by('-created_at')[:3],
            'sliders': ProductModel.objects.order_by('created_at')[:3],
            'products': ProductModel.objects.all(),
            'categories': CategoryModel.objects.all()
        }
        return render(request, 'index.html', context=context)

class AboutView(ListView):
    model = BrandModel
    template_name = 'about.html'
    context_object_name = 'brands'

    def get_context_data(self, **kwargs):
        context =  super(AboutView, self).get_context_data(**kwargs)
        context['team'] = TeamModel.objects.all()[:3]
        return context

class ContactView(SuccessMessageMixin, CreateView):
    model = ContactModel
    form_class = ContactModelForm
    template_name = 'contact.html'
    success_message = 'Your message has been taken into account, we will contact you soon.'

class TeamView(ListView):
    model = TeamModel
    template_name = 'team.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        context['brands'] = BrandModel.objects.all()
        return context

class SearchView(ListView):
    model = ProductModel
    template_name = 'search.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        return ProductModel.objects.filter(
            Q(name__icontains=query) | Q(tag__name__icontains=query) | Q(category__category_name__icontains= query)
        ).distinct()

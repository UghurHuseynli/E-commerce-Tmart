from django.shortcuts import redirect, render
from django.urls import reverse
from .models import ProductModel, ProductImgModel, ProductVersionModel, ProductColorModel, ProductSizeModel, ReviewsModel
from .forms import ReviewModelForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.

class ProductView(ListView):
    model = ProductModel
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 1
    max_paginate_by = 1

class ProductDetailView(DetailView, CreateView):
    model = ProductModel
    form_class = ReviewModelForm
    template_name = 'product-details.html'
    # success_message = 'Your review added.'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product_ver = ProductVersionModel.objects.filter(product_id = kwargs['object'].id).all()
        context['product_version'] = product_ver
        context['all_review'] = ReviewsModel.objects.filter(product_id = kwargs['object'].id)
        # context['images'] = ProductImgModel.objects.filter(product_version_id = product_ver[0].id).all() 
        context['review_form'] = ReviewModelForm()
        return context

    def post(self, request, *args, **kwargs):
        new_review = ReviewModelForm(request.POST, request.FILES)
        product = ProductModel.objects.get(slug = kwargs['slug'])
        if new_review.is_valid():
            new_review.instance.product_id = product
            new_review.instance.save()
            messages.success(request, 'Your review added.')
            return redirect(reverse('product_detail', kwargs={'slug': kwargs['slug']}))
        context = {
            'product': product,
            'product_version': ProductVersionModel.objects.filter(product_id = ProductModel.objects.get(slug = kwargs['slug'])).all(),
            'review_form': new_review
        }
        return render(request, 'product-details.html', context = context)

def customer_review(requests):
    return render(requests, 'customer-review.html')
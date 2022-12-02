from .models import BlogModel, CommentModel
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.db.models import Q
from .forms import CommentModelForm
from Product.models import CategoryModel, TagsModel
from django.shortcuts import redirect

# Create your views here.
class BlogView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 2

class BlogDetailsView(DetailView, CreateView):
    model = BlogModel
    template_name = 'blog-details.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'
    form_class = CommentModelForm

    def form_valid(self, form, *args, **kwargs):
        blog = BlogModel.objects.get(slug = self.kwargs.get('slug'))
        form.instance.blog = blog
        form.instance.save()
        messages.success(self.request, 'Your comments added.')
        return redirect("blog_details", blog.slug)
    

    def form_invalid(self, form):
        ctx = {}
        ctx['blog'] = BlogModel.objects.get(slug = self.kwargs.get('slug'))
        ctx['comments'] = CommentModel.objects.filter(blog = ctx['blog'].id).all()
        ctx['form'] = form
        return self.render_to_response(ctx)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentModel.objects.filter(blog = self.object.id).all()
        context['latest'] = BlogModel.objects.order_by('-created_at')[:5]
        context['tags'] = TagsModel.objects.all()
        context['categories'] = CategoryModel.objects.filter(is_navbar = True).all()
        return context

class BlogSearchView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search-blog')
        return BlogModel.objects.filter(
            Q(title__icontains=query) | Q(created_by__username__icontains=query) | Q(tag__name__icontains=query) | Q(category__category_name__icontains= query)
        ).distinct()

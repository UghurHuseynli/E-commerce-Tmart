from .models import BlogModel, CommentModel
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .forms import CommentModelForm
from django.shortcuts import redirect

# Create your views here.
class BlogView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 1

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
        return context

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('api/', include('Blog.api.urls')),
    path('api/', include('User.api.urls')),
    path('api/', include('Product.api.urls')),
    path('api/', include('Order.api.urls')),
    path('openapi/', get_schema_view(
        title="Tmart",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]

urlpatterns += i18n_patterns(
    path('', include('Core.urls')),
    path('account/', include('User.urls')),
    path('blog/', include('Blog.urls')),
    path('order/', include('Order.urls')),
    path('product/', include('Product.urls')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar 
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


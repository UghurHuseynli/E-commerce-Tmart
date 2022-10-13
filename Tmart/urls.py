from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('social_django.urls', namespace='social')),
]

urlpatterns += i18n_patterns(
    path('', include('Core.urls')),
    path('account/', include('User.urls')),
    path('blog/', include('Blog.urls')),
    path('api/', include('Blog.api.urls')),
    path('api/', include('User.api.urls')),
    path('order/', include('Order.urls')),
    path('product/', include('Product.urls')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
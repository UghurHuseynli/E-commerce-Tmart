from django.urls import path
from .views import index, about, ContactView, team
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name = 'about'),
    path('contact/', csrf_exempt(ContactView.as_view()), name = 'contact'),
    path('team/', team, name = 'team')
]
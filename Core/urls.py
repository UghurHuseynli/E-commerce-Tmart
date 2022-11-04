from django.urls import path
from .views import  about, ContactView, team, IndexView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name = 'about'),
    path('contact/', csrf_exempt(ContactView.as_view()), name = 'contact'),
    path('team/', team, name = 'team')
]
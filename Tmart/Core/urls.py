from django.urls import path
from .views import  AboutView, ContactView, TeamView, IndexView, SearchView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('contact/', csrf_exempt(ContactView.as_view()), name = 'contact'),
    path('team/', TeamView.as_view(), name = 'team'),
    path('search/', SearchView.as_view(), name='search')
]
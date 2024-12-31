from django.urls import path
from .views import SpamView, SearchView

urlpatterns = [
    path('spam/', SpamView.as_view(), name='mark_spam'),
    path('search/', SearchView.as_view(), name='search'),
]

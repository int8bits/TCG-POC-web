
from django.urls import path

from .views import MainView, ResumeDeckView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('resume_deck/<pk>', ResumeDeckView.as_view(), name='resume_deck'),
]

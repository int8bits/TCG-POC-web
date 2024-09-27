
from django.urls import path

from .views import FileCardsFormView

urlpatterns = [
    path('add/', FileCardsFormView.as_view(), name='file_cards'),
]

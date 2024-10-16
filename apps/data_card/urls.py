
from django.urls import path

from .router import router
from .views import (
    CardsListView,
    CardDetailView,
    CardUpdateView,
    CardProfferView
)

urlpatterns = [
    # path('add/', FileCardsFormView.as_view(), name='file_cards'),
    path("", CardsListView.as_view(), name="card_list"),
    path("<pk>/detail", CardDetailView.as_view(), name="card_detail"),
    path("<pk>/update", CardUpdateView.as_view(), name="card_update"),
    path(
        "<pk>/success", CardProfferView.as_view(), name="card_success_proffer"
    ),
] + router.urls

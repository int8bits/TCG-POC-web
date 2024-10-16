
from rest_framework.routers import DefaultRouter

from .api import CardViewSet


router = DefaultRouter()
router.register(r"api/cards", CardViewSet, basename="api")

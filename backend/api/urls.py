from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnkiDeckViewSet

router = DefaultRouter()
router.register(r'decks', AnkiDeckViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from rest_framework import viewsets
from .models import AnkiDeck
from .serializers import AnkiDeckSerializer

class AnkiDeckViewSet(viewsets.ModelViewSet):
    queryset = AnkiDeck.objects.all()
    serializer_class = AnkiDeckSerializer
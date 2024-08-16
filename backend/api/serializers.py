from rest_framework import serializers
from .models import AnkiDeck

class AnkiDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnkiDeck
        fields = ['id', 'name', 'file', 'uploaded_at']
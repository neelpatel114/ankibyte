from django.db import models

class AnkiDeck(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='anki_decks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=150)
    expansion = models.CharField(max_length=100)
    card_number = models.CharField(max_length=20)
    rarity = models.CharField(max_length=50)
    language = models.CharField(max_length=30, default='English')
    image_url = models.URLField(
        max_length=500,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.expansion}"
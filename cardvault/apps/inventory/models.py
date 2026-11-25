from django.db import models
from django.conf import settings
from apps.cards.models import Card


class Inventory(models.Model):

    CONDITION_CHOICES = [
        ('MINT', 'Mint'),
        ('NEAR_MINT', 'Near Mint'),
        ('EXCELLENT', 'Excellent'),
        ('GOOD', 'Good'),
        ('PLAYED', 'Played'),
        ('POOR', 'Poor'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inventory'
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.PROTECT,
        related_name='inventory_entries'
    )

    quantity = models.PositiveIntegerField(default=1)

    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='NEAR_MINT'
    )

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'card', 'condition'],
                name='unique_user_card_condition'
            ),
            models.CheckConstraint(
                condition=models.Q(quantity__gt=0),
                name='inventory_quantity_gt_zero'
            ),
        ]

    def __str__(self):
        return f"{self.card.name} - {self.user.username} ({self.quantity})"
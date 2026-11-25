from django.db import models
from apps.cards.models import Card
from apps.inventory.models import Inventory
from django.conf import settings


class Sale(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='sales'
    )

    sold_at = models.DateTimeField(auto_now_add=True)

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"Sale #{self.id} - {self.user.username}"

class SaleItem(models.Model):

    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name='items'
    )

    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.PROTECT,
        related_name='sale_items'
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.PROTECT,
        related_name='sale_items'
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.card.name} x{self.quantity}"

    @property
    def subtotal(self):
        return self.quantity * self.unit_price
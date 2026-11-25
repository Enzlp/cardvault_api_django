from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from apps.cards.filters import CardFilter
from apps.cards.models import Card
from apps.cards.pagination import CardPagination
from apps.cards.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.order_by("id")
    serializer_class = CardSerializer
    pagination_class = CardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CardFilter
    search_fields = ["name", "expansion", "card_number"]
    ordering_fields = ["id", "name", "expansion", "rarity", "created_at"]
    ordering = ["id"]
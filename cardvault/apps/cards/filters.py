import django_filters
from apps.cards.models import Card


class CardFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    expansion = django_filters.CharFilter(field_name="expansion", lookup_expr="iexact")
    rarity = django_filters.CharFilter(field_name="rarity", lookup_expr="iexact")
    language = django_filters.CharFilter(field_name="language", lookup_expr="iexact")
    card_number = django_filters.CharFilter(field_name="card_number", lookup_expr="iexact")

    class Meta:
        model = Card
        fields = ["name", "expansion", "rarity", "language", "card_number"]
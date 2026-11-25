
import pytest
from django.utils import timezone

from apps.cards.models import Card


@pytest.mark.django_db
class TestCardModel:

    def test_create_card(self):
        card = Card.objects.create(
            name="Charizard",
            expansion="Base Set",
            card_number="4/102",
            rarity="Holo Rare",
            language="English"
        )

        assert card.id is not None
        assert card.name == "Charizard"
        assert card.expansion == "Base Set"
        assert card.card_number == "4/102"
        assert card.rarity == "Holo Rare"
        assert card.language == "English"

    def test_default_language(self):
        card = Card.objects.create(
            name="Pikachu",
            expansion="Base Set",
            card_number="58/102",
            rarity="Common"
        )

        assert card.language == "English"

    def test_image_url_is_optional(self):
        card = Card.objects.create(
            name="Mewtwo",
            expansion="Base Set",
            card_number="10/102",
            rarity="Rare"
        )

        assert card.image_url is None

    def test_create_card_with_image_url(self):
        url = "https://example.com/charizard.jpg"

        card = Card.objects.create(
            name="Charizard",
            expansion="Base Set",
            card_number="4/102",
            rarity="Holo Rare",
            image_url=url
        )

        assert card.image_url == url

    def test_card_str(self):
        card = Card.objects.create(
            name="Charizard",
            expansion="Base Set",
            card_number="4/102",
            rarity="Holo Rare"
        )

        assert str(card) == "Charizard - Base Set"

    def test_created_at_is_set(self):
        card = Card.objects.create(
            name="Pikachu",
            expansion="Base Set",
            card_number="58/102",
            rarity="Common"
        )

        assert card.created_at is not None
        assert card.created_at <= timezone.now()

    def test_updated_at_is_set(self):
        card = Card.objects.create(
            name="Pikachu",
            expansion="Base Set",
            card_number="58/102",
            rarity="Common"
        )

        assert card.updated_at is not None
        assert card.updated_at <= timezone.now()

    def test_updated_at_changes_when_card_is_saved(self):
        card = Card.objects.create(
            name="Pikachu",
            expansion="Base Set",
            card_number="58/102",
            rarity="Common"
        )

        original_updated_at = card.updated_at

        card.name = "Pikachu V"
        card.save()

        assert card.updated_at >= original_updated_at
        assert card.name == "Pikachu V"

from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    TEXT_FIELDS = ["name", "expansion", "card_number", "rarity", "language"]

    class Meta:
        model = Card
        fields = [
            "id",
            "name",
            "expansion",
            "card_number",
            "rarity",
            "language",
            "image_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, attrs):
        for field in self.TEXT_FIELDS:
            if field in attrs and isinstance(attrs[field], str):
                cleaned = attrs[field].strip()
                if not cleaned:
                    raise serializers.ValidationError({field: "Este campo no puede estar vacío."})
                attrs[field] = cleaned

        if "language" in attrs:
            attrs["language"] = attrs["language"].title()

        name = attrs.get("name", getattr(self.instance, "name", None))
        expansion = attrs.get("expansion", getattr(self.instance, "expansion", None))
        card_number = attrs.get("card_number", getattr(self.instance, "card_number", None))
        language = attrs.get("language", getattr(self.instance, "language", None))

        if all(val is not None for val in (name, expansion, card_number, language)):
            qs = Card.objects.filter(
                name__iexact=name,
                expansion__iexact=expansion,
                card_number__iexact=card_number,
                language__iexact=language,
            )
            if self.instance is not None:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError(
                    "Ya existe una carta con el mismo nombre, expansión, número y idioma."
                )

        return attrs
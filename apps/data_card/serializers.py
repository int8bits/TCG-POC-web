
from rest_framework import serializers

from .models import (
    Card,
)


class CardListSerializer(serializers.ModelSerializer):
    kind = serializers.CharField(source="kind.name", default=None)
    generation = serializers.CharField(source="generation.name", default=None)
    element = serializers.CharField(source="element.name", default=None)

    class Meta:
        model = Card
        fields = [
            "id",
            "name",
            "attack",
            "rest",
            "image",
            "kind",
            "generation",
            "element",
        ]


class CardDetailSerializer(serializers.ModelSerializer):
    element = serializers.CharField(source="element.name", default=None)
    generation = serializers.CharField(source="generation.name", default=None)
    kind = serializers.CharField(source="kind.name", default=None)
    rarity = serializers.CharField(source="rarity.name", default=None)
    original_deck = serializers.CharField(
        source="original_deck.name",
        default=None
    )

    class Meta:
        model = Card
        fields = "__all__"


from rest_framework import serializers

from .models import (
    Card,
    Element,
    Generation,
    Kind,
    Rarity,
    OriginalDeck,
)


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ["name"]


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = ["name"]


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ["name"]


class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = ["name"]


class OriginalDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginalDeck
        fields = ["name"]


class CardListSerializer(serializers.ModelSerializer):
    kind = KindSerializer()
    generation = GenerationSerializer()
    element = ElementSerializer()

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
    element = ElementSerializer()
    generation = GenerationSerializer()
    kind = KindSerializer()
    rarity = RaritySerializer()
    original_deck = OriginalDeckSerializer()

    class Meta:
        model = Card
        fields = "__all__"

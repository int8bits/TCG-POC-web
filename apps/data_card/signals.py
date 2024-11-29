
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    CardProffer,
    Card,
    Kind,
    Generation,
    Element,
    OriginalDeck,
    Rarity,
)


@receiver(post_save, sender=CardProffer)
def save_real_card(sender, instance, **kwargs):
    if sender.approved == True:
        kind = None
        generation = None
        element = None
        original_deck = None
        rarity = None

        if instance.kind is not None:
            kind = Kind.objects.get(id=instance.kind)
        if instance.generation is not None:
            generation = Generation.objects.get(id=instance.generation)
        if instance.element is not None:
            element = Element.objects.get(id=instance.element)
        if instance.original_deck is not None:
            original_deck = OriginalDeck.objects.get(id=instance.original_deck)
        if instance.rarity is not None:
            rarity = Rarity.objects.get(id=instance.rarity)

        card = Card.objects.get(id_k=instance.id_k)

        card.name=instance.name
        card.passive=instance.passive
        card.quick_passive=instance.quick_passive
        card.active=instance.active
        card.quick_active=instance.quick_active
        card.cost=instance.cost
        card.description=instance.description
        card.attack=instance.attack
        card.rest=instance.rest
        card.image=instance.image
        card.kind=kind
        card.generation=generation
        card.element=element
        card.original_deck=original_deck
        card.rarity=rarity

        card.save()

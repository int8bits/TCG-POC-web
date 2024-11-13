from django.db import models


class Deck(models.Model):
    name_deck = models.CharField(max_length=64)
    description = models.TextField()
    cards = models.ManyToManyField('data_card.Card', related_name='decks')
    user = models.ForeignKey(
        'user.ExtendedUser', on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CardNotFound(models.Model):
    id_k = models.CharField(max_length=16, unique=True)
    proffer = models.ForeignKey(
        'data_card.CardProffer',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    own_deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

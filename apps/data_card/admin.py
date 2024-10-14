from django.contrib import admin

from .models import (
    Card,
    Element,
    FileCards,
    Generation,
    Kind,
    OriginalDeck,
    Rarity
)


class CardAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "attack",
        "rest",
        "kind",
        "generation",
        "element",
        "original_deck",
    ]
    search_fields = ["name"]


admin.site.register(Card, CardAdmin)
admin.site.register(Element)
admin.site.register(FileCards)
admin.site.register(Generation)
admin.site.register(Kind)
admin.site.register(OriginalDeck)
admin.site.register(Rarity)
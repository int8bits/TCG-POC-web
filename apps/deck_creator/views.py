
from django.apps import apps
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect

from .models import Deck


class MainView(View):
    template_name = 'deck_creator/main.html'

    def get(self, request):
        return TemplateView.as_view(template_name=self.template_name)(request)

    def post(self, request):
        Card = apps.get_model('data_card', 'Card')
        not_founds = []
        cards_found = []
        name = request.POST.get('deckName')
        description = request.POST.get('deckDescription')
        card_list = request.POST.getlist('deckCards')

        print(name)
        print(description)
        print(card_list)

        for card_ in card_list:
            try:
                card = Card.objects.get(pk=card_)
                cards_found.append(card)
            except Card.DoesNotExist:
                not_founds.append(card_)

        deck = Deck.objects.create(
            name_deck=name,
            description=description,
            user=None,
            cards_not_found=not_founds
        )

        deck.cards.add(*cards_found)

        return redirect('resume_deck')


class ResumeDeckView(DetailView):
    template_name = 'deck_creator/resume_deck.html'
    model = Deck

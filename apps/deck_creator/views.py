
import importlib

from django.apps import apps
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .models import Deck, CardNotFound


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
        card_list = request.POST.get('deckCards')
        card_list = [
            card.strip() for card in card_list.split(',') if card.strip()
        ]

        for card_ in card_list:
            print(card_)
            try:
                card = Card.objects.get(id_k=card_)
                cards_found.append(card)
            except Card.DoesNotExist:
                not_founds.append(card_)

        deck = Deck.objects.create(
            name_deck=name,
            description=description,
            user=None,
        )

        deck.cards.add(*cards_found)

        if not_founds:
            for card in not_founds:
                CardNotFound.objects.create(
                    id_k=card,
                    own_deck=deck
                )

        return redirect(reverse('resume_deck', args=[deck.pk]))


class ResumeDeckView(View):
    template_name = 'deck_creator/resume_deck.html'
    model = Deck
    context_object_name = 'deck'

    def get(self, request, pk):
        forms_module = importlib.import_module('apps.data_card.forms')
        form_card_proffer = getattr(forms_module, 'CardProfferForm')

        deck = self.model.objects.get(pk=pk)
        context = {
            "adendei": [
                card for card in deck.cards.all()
                if 'Adendei' in card.kind.name
            ],
            "ixims": [
                card for card in deck.cards.all()
                if card.kind.name == 'Ixim'
            ],
            "rots": [
                card for card in deck.cards.all()
                if card.kind.name == 'Rot'
            ],
            "bio": [
                card for card in deck.cards.all()
                if card.kind.name == 'Bio'
            ],
            "protectors": [
                card for card in deck.cards.all()
                if card.kind.name == 'Protector'
            ],
            "not_found": deck.not_founds.all(),
            "form_card_proffer": form_card_proffer,
        }

        return TemplateView.as_view(
            template_name=self.template_name,
            extra_context=context,
        )(request)

    def post(self, request, pk):
        forms_module = importlib.import_module('apps.data_card.forms')
        form_card_proffer = getattr(forms_module, 'CardProfferForm')

        form = request.POST
        deck = self.model.objects.get(pk=pk)
        # print(form)
        form = form_card_proffer(form)

        if form.is_valid():
            proffer = form.save()

            proffer.save()
            card_not_found = CardNotFound.objects.get(
                id_k=form.cleaned_data['id_k'],
                own_deck=deck,
            )
            card_not_found.proffer = proffer
            card_not_found.save()

        print(form.errors)

        return redirect(reverse('resume_deck', args=[deck.pk]))

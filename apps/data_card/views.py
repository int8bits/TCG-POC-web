from django.urls import reverse_lazy
from django.views import generic

from .forms import FileCardsForm
from .models import Card, CardProffer


class FileCardsFormView(generic.FormView):
    template_name = 'data_card/add_file.html'
    form_class = FileCardsForm
    success_url = reverse_lazy('file_cards')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CardsListView(generic.ListView):
    template_name = 'data_card/card_list.html'
    context_object_name = 'card_list'
    model = Card
    paginate_by = 20
    ordering = ['id']


class CardDetailView(generic.DetailView):
    template_name = 'data_card/card_detail.html'
    context_object_name = 'card'
    model = Card


class CardUpdateView(generic.UpdateView):
    template_name = 'data_card/card_update.html'
    model = Card
    fields = [
        "id",
        "name",
        "passive",
        "quick_passive",
        "active",
        "quick_active",
        "cost",
        "description",
        "attack",
        "rest",
        "image",
        "kind",
        "generation",
        "element",
        "original_deck",
        "rarity",
    ]

    def get_success_url(self) -> str:
        # return reverse_lazy('card_list')
        return reverse_lazy(
            'card_success_proffer', kwargs={'pk': self.pk_proffer}
        )

    def form_valid(self, form):
        card = form.save(commit=False)
        proffer = CardProffer.objects.create(
            id_k=card.id,
            name=card.name,
            passive=card.passive,
            active=card.active,
            quick_passive=card.quick_passive,
            quick_active=card.quick_active,
            cost=card.cost,
            description=card.description,
            attack=card.attack,
            rest=card.rest,
            banned=card.banned,
            image=card.image,
            kind=card.kind.id,
            generation=card.generation.id,
            element=card.element.id,
            original_deck=card.original_deck.id,
            rarity=card.rarity.id if card.rarity is not None else None,
        )

        self.pk_proffer = proffer.pk

        return super().form_valid(form)


class CardProfferView(generic.DetailView):
    template_name = 'data_card/success_request.html'
    context_object_name = 'card_proffer'
    model = CardProffer
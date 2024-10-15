from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

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


class CardDetailView(generic.DetailView):
    template_name = 'data_card/card_detail.html'
    context_object_name = 'card'
    model = Card


class CardUpdateView(generic.UpdateView):
    template_name = 'data_card/card_update.html'
    model = Card
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('card_list')
        # return reverse_lazy('card_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        card = form.save(commit=False)
        print(card)
        # proffer = CardProffer.objects.create(
        #     id_k=card.id_k,
        #     name=card.name,
        #     passive=card.passive,
        #     active=card.active,
        #     quick_passive=card.quick_passive,
        #     quick_active=card.quick_active,
        #     cost=card.cost,
        #     description=card.description,
        #     attack=card.attack,
        #     rest=card.rest,
        #     banned=card.banned,
        #     image=card.image,
        #     kind=card.kind.id,
        #     generation=card.generation.id,
        #     element=card.element.id,
        #     original_deck=card.original_deck.id,
        #     rarity=card.rarity.id,
        # )

        return super().form_valid(form)


class CardProfferView(generic.DetailView):
    template_name = 'data_card/card_proffer.html'
    context_object_name = 'card_proffer'
    model = CardProffer
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import FileCardsForm

# Create your views here.
class FileCardsFormView(generic.FormView):
    template_name = 'data_card/add_file.html'
    form_class = FileCardsForm
    success_url = reverse_lazy('file_cards')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
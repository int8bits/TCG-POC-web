
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'deck_creator/main.html'

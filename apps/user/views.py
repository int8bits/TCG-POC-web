
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login as auth_login

from .forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return super().form_valid(form)

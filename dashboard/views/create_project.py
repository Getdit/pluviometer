from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Project

class CreateProject(LoginRequiredMixin, CreateView):
    template_name = 'main.html'
    model = Project
    fields = ['name', 'description']

    def get_success_url(self):
        obj = self.object
        return reverse('dashboard:project', kwargs={'pk': obj.pk})

    def form_valid(self, form):
        if self.request.user.profile.is_researcher:
            print("Sucesso")
            return super().form_valid(form)
        else:
            print("Falha")
            return super().form_invalid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

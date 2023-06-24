from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from core.models import Project

class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/projects.html'
    model = Project

class ProjectView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/project.html'
    model = Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main.html'
    model = Project
    fields = ['name', 'description']

    def get_success_url(self):
        obj = self.object
        return reverse('dashboard:project_detail', kwargs={'pk': obj.pk})

    def form_valid(self, form):
        if self.request.user.profile.is_researcher:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'main.html'
    model = Project
    fields = ['name', 'description']

    def get_success_url(self):
        obj = self.object
        return reverse('dashboard:project_detail', kwargs={'pk': obj.pk})

    def form_valid(self, form):
        if self.request.user.profile.is_researcher:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'main.html'
    model = Project

    def get_success_url(self):
        return reverse('dashboard:project_list')

    def form_valid(self, form):
        if self.request.user.profile.is_researcher:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
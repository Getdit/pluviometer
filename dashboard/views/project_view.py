from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Project

class ProjectView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/project.html'
    model = Project
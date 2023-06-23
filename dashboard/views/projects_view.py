from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Project
class ProjectsView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/projects.html'
    model = Project

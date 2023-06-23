from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from accounts.models import Profile

class ProjectsUsersView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/project_users.html'

    def get_queryset(self):
        return Profile.objects.filter(projects__id=self.kwargs['pk'])

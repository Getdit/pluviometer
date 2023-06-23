from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from core.models import Device

class ProjectsSensorsView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/project_sensors.html'
    model = Device

    def get_queryset(self):
        return self.model.objects.filter(project=self.kwargs['pk'])

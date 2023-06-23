from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Alert

class ListProjectAlerts(LoginRequiredMixin,ListView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert

    def get_queryset(self):
        return self.model.objects.filter(project=self.kwargs['pk'])
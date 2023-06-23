from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Alert

class DeleteProjectAlert(LoginRequiredMixin,DeleteView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert

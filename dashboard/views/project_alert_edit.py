from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Alert

class UpdateProjectAlert(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert
    fields = ['name', 'description', 'formula', 'devices']

    def get_queryset(self):
        return self.model.objects.filter(project=self.kwargs['pk'])
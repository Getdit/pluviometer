from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Alert

class CreateProjectAlert(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert
    fields = ['name', 'description', 'formula', 'devices']

    def form_valid(self, form):
        form.instance.project = self.kwargs['pk']
        return super().form_valid(form)

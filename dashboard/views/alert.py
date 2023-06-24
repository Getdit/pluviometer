from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from core.models import Alert, Project, Device

from core.forms import AlertForm


class AlertCreateView(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert
    fields = ['name', 'description', 'formula', 'devices']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project = Project.objects.get(id=self.kwargs['pk'])
        obj.save()

        if not obj.formula_validation():
            obj.delete()
            raise Exception("Invalid formula")
        else:
            obj.devices.set(form.cleaned_data['devices'])
            obj.save()

        return HttpResponseRedirect(self.get_success_url(obj.id))

    def get_success_url(self, id):
        return reverse('dashboard:project_alert_list', kwargs={'pk': self.kwargs['pk']})

class AlertDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert

    def get_success_url(self):
        return reverse('dashboard:project_alert_list', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        return get_object_or_404(Alert, pk=self.kwargs['alert_pk'], project=self.kwargs['pk'])

class AlertUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert
    fields = ['name', 'description', 'formula', 'devices']

    def get_queryset(self):
        return self.model.objects.filter(project=self.kwargs['pk'])

class AlertListView(LoginRequiredMixin,ListView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert

    def get_queryset(self):
        return self.model.objects.filter(project=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['devices'] = Device.objects.all()
        context['project'] = self.kwargs['pk']
        context['form'] = AlertForm()
        return context
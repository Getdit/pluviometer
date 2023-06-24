from django.views.generic import ListView, FormView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse, HttpResponseRedirect, HttpResponse
from django.core.files.base import ContentFile
from django.http import FileResponse
from django.utils import timezone

from core.models import Device, Project
from core.forms import AssignDeviceProjectForm


from io import StringIO


class DeviceListView(LoginRequiredMixin,ListView):
    template_name = 'dashboard/device_list.html'
    model = Device

class DeviceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/device_create.html'
    model = Device
    fields = ['mac', 'model', 'location', 'latitude', 'longitude']

    def get_success_url(self):
        return reverse('dashboard:device_list')

class DeviceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/device_update.html'
    model = Device
    fields = ['mac', 'model', 'location', 'latitude', 'longitude']

    def get_success_url(self):
        return reverse('dashboard:device_list')

class DeviceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'dashboard/device_delete.html'
    model = Device

    def get_success_url(self):
        return reverse('dashboard:device_list')

class DeviceLogsView(View):
    template_name = 'dashboard/sensor_reads.html'

    def get(self, request, *args, **kwargs):
        period_ref = {'one_day':1, 'three_days':3, 'five_days':5, 'seven_days':7, }
        period = period_ref[self.kwargs['period']]
        time = timezone.now() - timezone.timedelta(days=period)
        str_now = timezone.now().strftime('%Y-%m-%d')

        device = Device.objects.get(id=self.kwargs['pk'])
        headers = [x.reference_tag for x in device.model.datamodel_set.all()]
        logs = device.devicelog_set.filter(created_at__gte=time)
        output = 'date;' + ';'.join(headers)+'\n'

        for log in logs:
            output += str(log.created_at)+';' + ';'.join([str(log.datalog_set.filter(model__reference_tag=x).first().value) for x in headers])+'\n'

        file_to_send = ContentFile(output)
        response = HttpResponse(file_to_send, 'application/x-gzip')
        response['Content-Length'] = file_to_send.size
        response['Content-Disposition'] = f'attachment; filename="device_{device.mac.upper().replace(":", "_")}_logs_{str_now}_{self.kwargs["period"]}"'
        return response

class ProjectDeviceListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/project_sensors.html'
    model = Device

    def get_queryset(self):
        return self.model.objects.filter(project=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.kwargs['pk']
        return context

class ProjectDeviceAddView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/project_sensors.html'
    form_class = AssignDeviceProjectForm

    def form_valid(self, form):
        project = Project.objects.get(id=self.kwargs['pk'])

        device = Device.objects.get(mac=form.clean_profile()).id
        project.device_set.add(device)
        project.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('dashboard:project_devices_list', kwargs={'pk': self.kwargs['pk']})

class ProjectDeviceRemoveView(LoginRequiredMixin, View):
    template_name = 'dashboard/project_sensors.html'
    form_class = AssignDeviceProjectForm

    def post(self, request, *args, **kwargs):
        if self.request.user.profile.is_researcher or self.request.user.profile.projects.filter(id=self.kwargs['pk']).exists():
            project = Project.objects.get(id=self.kwargs['pk'])
            project.device_set.remove(self.kwargs['device_pk'])
            project.save()

        return super().HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('dashboard:project_user_list', kwargs={'pk': self.kwargs['pk']})

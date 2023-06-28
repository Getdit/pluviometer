from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse, HttpResponseRedirect

from core.models import DeviceModel, Firmware

class DeviceModelListView(LoginRequiredMixin,ListView):
    template_name = 'dashboard/device_model_list.html'
    model = DeviceModel

class DeviceModelDetailView(LoginRequiredMixin,DetailView):
    template_name = 'dashboard/device_model.html'
    model = DeviceModel

class DeviceModelCreateView(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/device_model.html'
    model = DeviceModel
    fields = ['name']

    def get_success_url(self):
        obj = self.object
        return reverse('dashboard:device_model_detail', kwargs={'pk': obj.pk})

class DeviceModelUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/device_model.html'
    model = DeviceModel
    fields = ['name']

    def get_success_url(self):
        obj = self.object
        return reverse('dashboard:device_model_detail', kwargs={'pk': obj.pk})

class DeviceModelDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'dashboard/device_model.html'
    model = DeviceModel

    def get_success_url(self):
        return reverse('dashboard:device_model_list')

class DeviceModelFirmwareCreateView(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/device_model.html'
    model = Firmware
    fields = ['detail', 'version', 'file']

    def get_success_url(self):
        return reverse('dashboard:device_models_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.model = DeviceModel.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

class DeviceModelFirmareUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/device_model.html'
    model = Firmware
    fields = ['detail', 'version', 'file']

    def get_success_url(self):
        return reverse('dashboard:device_models_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.model = DeviceModel.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

class DeviceModelFirmwareDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'dashboard/device_model.html'
    model = Firmware

    def get_success_url(self):
        return reverse('dashboard:device_models_detail', kwargs={'pk': self.kwargs['pk']})
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse, HttpResponseRedirect

from core.models import DataModel, DeviceModel


class DataModelCreateView(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/device_model.html'
    model = DataModel
    fields = ['name', 'description', 'reference_tag']

    def form_valid(self, form):
        form.instance.model = DeviceModel.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:device_models_detail', kwargs={'pk': self.kwargs['pk']})

class DataModelUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/device_model.html'
    model = DataModel
    fields = ['name', 'description', 'reference_tag']

    def get_success_url(self):
        return reverse('dashboard:device_models_detail', kwargs={'pk': self.kwargs['pk']})

class DataModelDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'dashboard/device_model.html'
    model = DataModel

    def get_success_url(self):
        return reverse('dashboard:device_models_detail', kwargs={'pk': self.kwargs['pk']})

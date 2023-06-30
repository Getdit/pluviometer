from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404

from core.models import Location
from core.forms import LocationForm


class LocationCreateView(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/locations_list.html'
    model = Location
    form_class = LocationForm

    def get_success_url(self):
        return reverse('dashboard:location_list')

class LocationDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'dashboard/locations_list.html'
    model = Location

    def get_success_url(self):
        return reverse('dashboard:location_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Location, pk=self.kwargs['pk'])

class LocationUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/locations_list.html'
    model = Location
    form_class = LocationForm

    def get_success_url(self):
        return reverse('dashboard:location_list')

class LocationListView(LoginRequiredMixin,ListView):
    template_name = 'dashboard/locations_list.html'
    model = Location

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LocationForm()
        context['search'] = self.request.GET.get('search') or ""
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = self.model.objects.all()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

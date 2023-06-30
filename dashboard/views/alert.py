from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.http import JsonResponse
from core.models import Alert, Project, Device

from core.forms import AlertForm


class AlertCreateView(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert
    fields = ['name', 'description', 'formula', 'devices']

    def form_valid(self, form):
        if self.request.user.profile.is_researcher or self.request.user.profile.projects.filter(
            id=self.kwargs['pk']).exists():
            obj = form.save(commit=False)
            obj.project = Project.objects.get(id=self.kwargs['pk'])
            obj.save()

            for device in form.cleaned_data['devices']:
                obj.devices.add(device)

            obj.save()

            if not obj.formula_validation():
                obj.delete()
                raise Exception("Invalid formula")
            else:
                obj.devices.set(form.cleaned_data['devices'])
                obj.save()

            return HttpResponseRedirect(self.get_success_url(obj.id))
        return super(AlertCreateView, self).form_invalid(form)

    def get_success_url(self, id):
        return reverse('dashboard:project_alert_list', kwargs={'pk': self.kwargs['pk']})

class AlertDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert
    fields = ['name', 'description', 'formula', 'devices']

    def form_valid(self, form):
        if self.request.user.profile.is_researcher or self.request.user.profile.projects.filter(
            id=self.kwargs['pk']).exists():
            return super().form_valid(form)
        return super(AlertUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:project_alert_list', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        return get_object_or_404(Alert, pk=self.kwargs['alert_pk'], project=self.kwargs['pk'])

class AlertUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/project_alert_list.html'
    model = Alert
    fields = ['name', 'description', 'formula', 'devices']

    def form_valid(self, form):
        if self.request.user.profile.is_researcher or self.request.user.profile.projects.filter(
            id=self.kwargs['pk']).exists():
            return super().form_valid(form)
        return super(AlertUpdateView, self).form_valid(form)

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
        context['has_permissions'] = self.request.user.profile.is_researcher or self.request.user.profile.projects.filter(
            id=self.kwargs['pk']).exists()
        return context

@csrf_exempt
def get_devices_params(request):
    if request.method == "POST":
        devices = map(int, request.POST.get('devices[]'))
        params = []
        root_params = []

        for x in Device.objects.filter(id__in=devices):
            for y in x.model.datamodel_set.all():
                root_params.append(y.reference_tag)


        for rp in root_params:
            params.append(rp)
            # params.extend(
            #     [
            #         f"{rp}:temp_1h",
            #         f"{rp}:temp_3h",
            #         f"{rp}:temp_5h",
            #         f"{rp}:temp_10h",
            #         f"{rp}:temp_15h",
            #         f"{rp}:temp_20h",
            #         f"{rp}:temp_1d",
            #         f"{rp}:temp_2d",
            #         f"{rp}:temp_3d"
            #     ]
            # )

        return JsonResponse({'params': f"[{'] ['.join(params)}]"})

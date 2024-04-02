from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.utils.html import escapejs

import plotly.graph_objs as go

from core.models import Project, DataModel, DeviceLog

class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/projects.html'
    model = Project
    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = self.model.objects.all()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search') or ""
        return context

class ProjectView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/project.html'
    model = Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main.html'
    model = Project
    fields = ['name', 'description']

    def get_success_url(self):
        obj = self.object
        return reverse('dashboard:project_detail', kwargs={'pk': obj.pk})

    def form_valid(self, form):
        if self.request.user.profile.is_researcher:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'main.html'
    model = Project
    fields = ['name', 'description']

    def get_success_url(self):
        obj = self.object
        return reverse('dashboard:project_detail', kwargs={'pk': obj.pk})

    def form_valid(self, form):
        if self.request.user.profile.is_researcher:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'main.html'
    model = Project

    def get_success_url(self):
        return reverse('dashboard:project_list')

    def form_valid(self, form):
        if self.request.user.profile.is_researcher:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

class ProjectChartFormView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/chart-form.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            data = self.request.GET.get('data', "").split('_')[:-1]

            start_date_str = self.request.GET.get('start_date')
            end_date_str = self.request.GET.get('end_date')
            start_date = None
            end_date = None

            if start_date_str:
                start_date = timezone.datetime.strptime(start_date_str, "%Y-%m-%d")

            if end_date_str:
                end_date = timezone.datetime.strptime(end_date_str, "%Y-%m-%d")

        except Exception as e:
            print(e)
            return context

        context['main_graph'] = ""

        if not data:
            return context

        traces = []
        labels = []

        for item in data:
            device_id, model_id, type_code =  map(int, item.split(';'))
            model = DataModel.objects.get(pk=model_id)

            y_values = []
            x_values = []
            device_data = DeviceLog.objects.filter(device_id=device_id).count()

            if start_date and not end_date:
                device_data = DeviceLog.objects.filter(device_id=device_id, created_at__gte=start_date)

            elif (not start_date) and end_date:
                device_data = DeviceLog.objects.filter(device_id=device_id, created_at__lte=end_date)

            elif start_date and end_date:
                device_data = DeviceLog.objects.filter(device_id=device_id, created_at__gte=start_date, created_at__lte=end_date)

            else:
                device_data = DeviceLog.objects.filter(device_id=device_id)

            for log in device_data:
                for dl in log.datalog_set.filter(model=model):
                    y_values.append(dl.value)
                    x_values.append(log.created_at)
            labels.append(model.name)

            if type_code == 0:
                traces.append(go.Bar(x=x_values, y=y_values, text="symbol", name=model.name))
            elif type_code == 1:
                traces.append(go.Scatter(x=x_values, y=y_values, text="symbol", name=model.name))

        layout = go.Layout(title=f"Gráfico gerado: {', '.join(labels)}",
                           xaxis_title="Data", yaxis_title="")

        # Criar a figura do gráfico com base no traço e layout criados anteriormente
        fig = go.Figure(data=traces, layout=layout)

        # Converter a figura para JSON para ser exibida na página da web
        context['main_graph'] = escapejs(fig.to_json())
        return context

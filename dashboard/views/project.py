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
        print(1)
        try:
            data = self.request.GET.get('data', "").split('_')
            start_date = timezone.datetime.strptime(self.request.GET.get('start_date'), "%Y-%m-%d")
            end_date = timezone.datetime.strptime(self.request.GET.get('end_date'), "%Y-%m-%d")
        except:
            return context
        print(2)
        if not data[0]:
            return context
        print(3)
        traces = []
        labels = []

        for item in data:

            print(4, data)
            device_id, model_id, type_code =  map(int, item.split(';'))
            model = DataModel.objects.get(pk=model_id)

            y_values = []
            x_values = []

            for log in DeviceLog.objects.filter(device_id=device_id, created_at__gte=start_date, created_at__lte=end_date):
                for dl in log.datalog_set.filter(model=model):
                    y_values.append(dl.value)
                    x_values.append(log.created_at)
            labels.append(model.name)
            if type_code == 0:
                traces.append(go.Scatter(x=x_values, y=y_values, text="symbol", name=model.name))
            elif type_code == 1:
                traces.append(go.Scatter(x=x_values, y=y_values, text="symbol", name=model.name))
        print(5)
        layout = go.Layout(title=f"Gráfico gerado: {', '.join(labels)}",
                           xaxis_title="Data", yaxis_title="")
        print(6)
        # Criar a figura do gráfico com base no traço e layout criados anteriormente
        fig = go.Figure(data=traces, layout=layout)
        print(7)
        # Converter a figura para JSON para ser exibida na página da web
        context['main_graph'] = escapejs(fig.to_json())
        return context

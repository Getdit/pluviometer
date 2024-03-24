from django.db import models
import plotly.graph_objs as go
from django.utils.html import escapejs
from django.utils import timezone

from core.models import DeviceLog
class Chart(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Projeto', related_name='charts')

    class Meta:
        verbose_name = 'Gráfico'
        verbose_name_plural = 'Gráficos'

    def __str__(self):
        return self.name

    def plot_json(self):
        traces = []
        labels = []

        for label in self.chartlabel_set.all():
            labels.append(label.name)
            traces.append(label.get_traces())

        # Configurar layout do gráfico
        layout = go.Layout(title=f"Últimos 7 dias: {', '.join(labels)}",
                           xaxis_title="Data", yaxis_title="")

        # Criar a figura do gráfico com base no traço e layout criados anteriormente
        fig = go.Figure(data=traces, layout=layout)

        # Converter a figura para JSON para ser exibida na página da web
        plot_json = escapejs(fig.to_json())
        return plot_json


class CHART_LABELS_TYPE(models.TextChoices):
    LINE = 'line', 'Linha'
    BAR = 'bar', 'Barra'
    # PIE = 'pie', 'Pizza'
    # SCATTER = 'scatter', 'Dispersão'
    # HEATMAP = 'heatmap', 'Mapa de Calor'
    # HISTOGRAM = 'histogram', 'Histograma'
    # BOXPLOT = 'boxplot', 'Boxplot'
    # AREA = 'area', 'Área'

class ChartLabel(models.Model):
    chart = models.ForeignKey('Chart', on_delete=models.CASCADE, verbose_name='Gráfico', related_name='data')
    name = models.CharField(max_length=255, verbose_name='Nome')

    type = models.CharField(max_length=255, verbose_name='Tipo', choices=CHART_LABELS_TYPE.choices)

    device = models.ForeignKey('Device', on_delete=models.CASCADE, verbose_name='Dispositivo', related_name='labels')
    datamodel = models.ForeignKey('DataModel', on_delete=models.CASCADE, verbose_name='Modelo de Dados', related_name='labels')

    class Meta:
        verbose_name = 'Dado do Gráfico'
        verbose_name_plural = 'Dados do Gráfico'

    def __str__(self):
        return self.chart.name

    def get_traces(self):
        x_values = []
        y_values = []

        for log in self.device.devicelog_set.filter(created_at__gte=(timezone.now() - timezone.timedelta(days=7))):
            for data in log.datalog_set.filter(model=self.datamodel):
                y_values.append(data.value)
                x_values.append(log.created_at)

        if self.type == CHART_LABELS_TYPE.LINE:
            return go.Scatter(x=x_values, y=y_values, text="symbol", name=self.name)
        elif self.type == CHART_LABELS_TYPE.BAR:
            return go.Bar(x=x_values, y=y_values, text="symbol", name=self.name)
        # elif self.type == CHART_LABELS_TYPE.PIE:
        #     return go.Pie(values=y_values, labels=x_values)
        # elif self.type == CHART_LABELS_TYPE.SCATTER:
        #     return go.Scatter(x=x_values, y=y_values, mode="markers")
        else:
            return go.Scatter(x=x_values, y=y_values, text="symbol")
from django.db import models
from django import forms
from django.utils.html import escapejs
from django.utils import timezone
import plotly.graph_objs as go

import datetime

class Device(models.Model):
    mac = models.CharField(max_length=30, verbose_name="MAC", unique=True)
    model = models.ForeignKey("core.DeviceModel", on_delete=models.CASCADE, verbose_name="Modelo")

    last_call = models.DateTimeField(verbose_name="Última chamada", null=True, blank=True)

    location = models.ForeignKey("core.Location", on_delete=models.CASCADE, verbose_name="Local")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    project = models.ManyToManyField("core.Project", verbose_name="Projeto")

    graph_data_models = models.ManyToManyField("core.DataModel", verbose_name="Modelos de dados para o gráfico",
                                               blank=True)

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        r = super(Device, self).save()
        from mqtt.utils import client
        if client:
            client.subscribe(f"sensor/{self.mac.lower()}/out")
        return r

    def __str__(self):
        return f"{self.location}: {self.model} - {self.mac} "

    def set_logs(self, data, dt_str:str =None):
        log = self.devicelog_set.create(device=self.id)
        # if dt_str is None:
        #     log = self.devicelog_set.create(device=self.id)
        # else:
        #     dt = datetime.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S-%z")
        #     log = self.devicelog_set.create(device=self.id, created_at=dt)

        for model_data in self.model.datamodel_set.all():
            if model_data.reference_tag in data.keys():
                log.datalog_set.create(
                    log=log,
                    model=model_data,
                    value=data[model_data.reference_tag]
                )
        print(f"LOG: {log} - {log.created_at} - {log.datalog_set.all()}")

        self.last_call = log.created_at
        self.save()

        self.verify_alerts()

    def verify_alerts(self):
        for project in self.project.all():
            for alert in project.alert_set.all():
                alert.verify()

    def get_form(self):
        class UpdateDevice(forms.ModelForm):
            class Meta:
                model = Device
                fields = ["mac", "model", "location", "latitude", "longitude", "graph_data_models"]

            def __init__(self, *args, **kwargs):
                super(UpdateDevice, self).__init__(*args, **kwargs)
                self.fields['graph_data_models'].queryset = self.instance.model.datamodel_set.all()

        return UpdateDevice(instance=self)

    def plot_json(self):
        tipo_de_grafico = "line"
        valor_x = None
        valor_y = None
        traces = []
        labels = []
        # Criar uma lista de valores x e y para o gráfico
        for datamodel in self.graph_data_models.all():
            y_values = []
            x_values = []

            for log in self.devicelog_set.filter(created_at__gte=(timezone.now() - timezone.timedelta(days=7))):
                for data in log.datalog_set.filter(model=datamodel):
                    y_values.append(data.value)
                    x_values.append(log.created_at)
            labels.append(datamodel.name)
            traces.append(go.Scatter(x=x_values, y=y_values, text="symbol", name=datamodel.name))

        # Criar o gráfico com Plotly
        #trace = None  # inicializar com um valor padrão

        #trace = go.Scatter(x=x_values, y=y_values, text="symbol")

        # if tipo_de_grafico == "line":
        #     trace = go.Scatter(x=x_values, y=y_values, text="symbol")
        # elif tipo_de_grafico == "bar":
        #     trace = go.Bar(x=x_values, y=y_values, text="symbol")
        # elif tipo_de_grafico == "pie":
        #     trace = go.Pie(values=y_values, labels=x_values)
        # elif tipo_de_grafico == "scatter":
        #     trace = go.Scatter(x=x_values, y=y_values, mode="markers")
        # elif tipo_de_grafico == "heatmap":
        #     trace = go.Heatmap(z=[[1, 20, 30], [20, 1, 60], [30, 60, 1]])
        # elif tipo_de_grafico == "histogram":
        #     trace = go.Histogram(x=y_values)
        # elif tipo_de_grafico == "boxplot":
        #     trace = go.Box(y=y_values)
        # elif tipo_de_grafico == "area":
        #     trace = go.Scatter(x=x_values, y=y_values, fill="tozeroy")
        # elif tipo_de_grafico == "scatter3d":
        #     trace = go.Scatter3d(x=x_values, y=y_values, z=[1, 2], mode="markers")
        # else:
        #     trace = go.Scatter(x=x_values, y=y_values,
        #                        text="symbol")  # valor padrão se o tipo de gráfico não for reconhecido

        # Configurar layout do gráfico
        layout = go.Layout(title=f"Últimos 7 dias: {', '.join(labels)}",
                           xaxis_title="Data", yaxis_title="")

        # Criar a figura do gráfico com base no traço e layout criados anteriormente
        fig = go.Figure(data=traces, layout=layout)

        # Converter a figura para JSON para ser exibida na página da web
        plot_json = escapejs(fig.to_json())
        return plot_json
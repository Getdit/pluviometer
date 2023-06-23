from django import forms
from django.shortcuts import render
from django.views import View
import plotly.graph_objs as go
from django.utils.html import escapejs
from core.models.data_model import DataModel
from django.db import models

class ChartForm(forms.Form):
    tipo_de_grafico = forms.ChoiceField(
        choices=[('line', 'Linha'), ('bar', 'Barras'), ('pie', 'Pizza'), ('scatter', 'Dispersão'), ('histogram', 'Histograma'), ('area', 'Área')], 
        required=False)
    valor_x = forms.ChoiceField(
        choices=[(f.name, f.verbose_name) for f in DataModel._meta.fields if isinstance(f, (models.FloatField, models.IntegerField, models.DecimalField))],
        required=False)
    valor_y = forms.ChoiceField(
        choices=[(f.name, f.verbose_name) for f in DataModel._meta.fields if isinstance(f, (models.FloatField, models.IntegerField, models.DecimalField))],
        required=False)

    def __init__(self, *args, **kwargs):
        super(ChartForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_grafico'].widget.attrs.update({
            'class': 'form-control custom-select'
        })
        self.fields['valor_x'].widget.attrs.update({
            'class': 'form-control custom-select'
        })
        self.fields['valor_y'].widget.attrs.update({
            'class': 'form-control custom-select'
        })


class ChartView(View):
    template_name = 'dashboard/chart.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = ChartForm(request.GET)
        if form.is_valid():
            tipo_de_grafico = form.cleaned_data['tipo_de_grafico']
            valor_x = form.cleaned_data['valor_x']
            valor_y = form.cleaned_data['valor_y']
        else:
            tipo_de_grafico = "line"
            valor_x = None
            valor_y = None

        # Criar uma lista de valores x e y para o gráfico
        x_values = ["teste1", "teste2", "teste3", "teste4", "teste5", "teste6"]
        y_values = [1,2,3,4,5,6]
        for obj in DataModel.objects.all():
            x_value = getattr(obj, valor_x) if valor_x else None
            y_value = getattr(obj, valor_y) if valor_y else None
            if x_value is not None and y_value is not None:
                x_values.append(x_value)
                y_values.append(y_value)

        # Criar o gráfico com Plotly
        trace = None  # inicializar com um valor padrão
       
        if tipo_de_grafico == "line":
            trace = go.Scatter(x=x_values, y=y_values, text="symbol")
        elif tipo_de_grafico == "bar":
            trace = go.Bar(x=x_values, y=y_values, text="symbol")
        elif tipo_de_grafico == "pie":
            trace = go.Pie(values=y_values, labels=x_values)
        elif tipo_de_grafico == "scatter":
            trace = go.Scatter(x=x_values, y=y_values, mode="markers")
        elif tipo_de_grafico == "heatmap":
            trace = go.Heatmap(z=[[1, 20, 30], [20, 1, 60], [30, 60, 1]])
        elif tipo_de_grafico == "histogram":
            trace = go.Histogram(x=y_values)
        elif tipo_de_grafico == "boxplot":
            trace = go.Box(y=y_values)
        elif tipo_de_grafico == "area":
            trace = go.Scatter(x=x_values, y=y_values, fill="tozeroy")
        elif tipo_de_grafico == "scatter3d":
            trace = go.Scatter3d(x=x_values, y=y_values, z=[1, 2], mode="markers")
        else:
            trace = go.Scatter(x=x_values, y=y_values, text="symbol")  # valor padrão se o tipo de gráfico não for reconhecido

        # Configurar layout do gráfico
        layout = go.Layout(title=f"Legenda do gráfico",
                           xaxis_title="ValoresX", yaxis_title="ValoresY")

        # Criar a figura do gráfico com base no traço e layout criados anteriormente
        fig = go.Figure(data=[trace], layout=layout)

        # Converter a figura para JSON para ser exibida na página da web
        plot_json = escapejs(fig.to_json())

        context = {
            'form': form,
            'plot_json': plot_json,
        }

        return render(request, self.template_name, context)


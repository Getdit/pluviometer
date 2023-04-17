from django.urls import path

from dashboard.views.chart_view import ChartView
from .views import DashboardView, ReportsView, SensorsView

app_name = "dashboard"

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('sensors/', SensorsView.as_view(), name='sensors'),
    path('chart/', ChartView.as_view(), name='chart'),
]
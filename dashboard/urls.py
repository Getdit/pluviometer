from django.urls import path
from .views import DashboardView, ReportsView, SensorsView, MapView

app_name = "dashboard"

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('sensors/', SensorsView.as_view(), name='sensors'),
    path('map/',  MapView.as_view(), name='map'),
]
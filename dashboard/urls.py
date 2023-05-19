from django.urls import path
from .views import DashboardView, ReportsView, SensorsView, MapView,LoginView,ProjectsView

app_name = "dashboard"

urlpatterns = [
    path('',  MapView.as_view(), name='map'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('account/',  LoginView.as_view(), name='account'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('sensors/', SensorsView.as_view(), name='sensors'),
    path('map/',  MapView.as_view(), name='map'),
    path('projects/',  ProjectsView.as_view(), name='projects'),
]
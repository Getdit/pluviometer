from django.urls import path
from .views import DashboardView, ReportsView, SensorsView
from .views import MapView,LoginView,ProjectsView,CreateView,ProjectView

app_name = "dashboard"

urlpatterns = [
    path('',  MapView.as_view(), name='map'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/',  LoginView.as_view(), name='login'),
    path('account/', CreateView.as_view(), name='account'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('sensors/', SensorsView.as_view(), name='sensors'),
    path('map/',  MapView.as_view(), name='map'),
    path('projects/',  ProjectsView.as_view(), name='projects'),
      path('project/',  ProjectView.as_view(), name='project'),
]
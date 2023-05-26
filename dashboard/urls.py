from django.urls import path

from dashboard.views.chart_view import ChartView
from dashboard.views.project_users_view import ProjectsUsersView
from dashboard.views.project_sensors_view import ProjectsSensorsView
from dashboard.views.sensor_reads import SensorReadsView

from .views import MapView,LoginView,ProjectsView,CreateView,ProjectView

app_name = "dashboard"

urlpatterns = [
    path('',  MapView.as_view(), name='map'),
    path('login/',  LoginView.as_view(), name='login'),
    path('projects/<int:id>/users/',
         ProjectsUsersView.as_view(), name='project_users'),
    path('projects/<int:id>/sensors/',
         ProjectsSensorsView.as_view(), name='project_sensors'),
    path('projects/<int:project_id>/sensors/<int:sensor_id>/reads',
         SensorReadsView.as_view(), name='sensor_reads'),
    path('projects/',  ProjectsView.as_view(), name='projects'),
    path('chart/',  ChartView.as_view(), name='chart'),
    path('account/', CreateView.as_view(), name='account'),               
    path('project/',  ProjectView.as_view(), name='project'),
]

from django.urls import path

from dashboard.views.chart_view import ChartView
from dashboard.views.project_users_view import ProjectsUsersView
from dashboard.views.project_sensors_view import ProjectsSensorsView
from dashboard.views.sensor_reads import SensorReadsView
from dashboard.views.project_view import ProjectView

from .views import MapView, ProjectsView, CreateProject, ListProjectAlerts, CreateProjectAlert, DeleteProjectAlert, UpdateProjectAlert

app_name = "dashboard"
urlpatterns = [
    path('',  MapView.as_view(), name='map'),

    path('projects/', ProjectsView.as_view(), name='projects'),
    path('project/create/', CreateProject.as_view(), name='create_project'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),
    #path('project/<int:pk>/edit/', ProjectView.as_view(), name='edit_project'),
    path('project/<int:pk>/alerts/', ListProjectAlerts.as_view(), name='project_alerts'),
    path('project/<int:pk>/alerts/create/', CreateProjectAlert.as_view(), name='create_project_alerts'),
    path('project/<int:pk>/alerts/<int:alert_pk>/edit/', UpdateProjectAlert.as_view(), name='update_project_alerts'),
    path('project/<int:pk>/alerts/<int:alert_pk>/delete/', DeleteProjectAlert.as_view(), name='delete_project_alerts'),
    path('projects/<int:pk>/users/', ProjectsUsersView.as_view(), name='project_users'),
    path('projects/<int:pk>/sensors/', ProjectsSensorsView.as_view(), name='project_sensors'),


    path('projects/<int:pk>/sensors/<int:sensor>/reads',
         SensorReadsView.as_view(), name='sensor_reads'),

    path('chart/',  ChartView.as_view(), name='chart'),

]




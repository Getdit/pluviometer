from django.urls import path

from dashboard.views.chart_view import ChartView
from .views import *

app_name = "dashboard"

urlpatterns = [
    path('',  MapView.as_view(), name='map'),

    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_detail'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    path('project/<int:pk>/alerts/', AlertListView.as_view(), name='project_alert_list'),
    path('project/<int:pk>/alerts/create/', AlertCreateView.as_view(), name='project_alert_create'),
    path('project/<int:pk>/alerts/<int:alert_pk>/update/', AlertUpdateView.as_view(), name='project_alert_update'),
    path('project/<int:pk>/alerts/<int:alert_pk>/delete/', AlertDeleteView.as_view(), name='project_alert_delete'),

    path('projects/<int:pk>/users/', ProjectUserListView.as_view(), name='project_user_list'),
    path('projects/<int:pk>/users/add/', ProjectAssignUserView.as_view(), name='project_user_add'),
    path('projects/<int:pk>/users/<int:user_pk>/remove/', ProjectUserRemoveView.as_view(), name='project_user_remove'),

    path('projects/<int:pk>/devices/', ProjectDeviceListView.as_view(), name='project_devices_list'),
    path('projects/<int:pk>/devices/add', ProjectDeviceAddView.as_view(), name='project_devices_add'),
    path('projects/<int:pk>/devices/<int:device_pk>/remove', ProjectDeviceRemoveView.as_view(), name='project_devices_remove'),

    path('devices/', DeviceListView.as_view(), name='devices_list'),
    path('devices/<int:pk>/create', DeviceCreateView.as_view(), name='device_create'),
    path('devices/<int:pk>/update', DeviceUpdateView.as_view(), name='device_update'),
    path('devices/<int:pk>/delete', DeviceDeleteView.as_view(), name='device_delete'),
    path('devices/<int:pk>/logs/<slug:period>/', DeviceLogsView.as_view(), name='device_logs'),

    path('device-models/', DeviceModelListView.as_view(), name='device_models_list'),
    path('device-models/create', DeviceModelCreateView.as_view(), name='device_models_create'),
    path('device-models/<int:pk>/', DeviceModelDetailView.as_view(), name='device_models_detail'),
    path('device-models/<int:pk>/update', DeviceModelUpdateView.as_view(), name='device_models_update'),
    path('device-models/<int:pk>/delete', DeviceModelDeleteView.as_view(), name='device_models_delete'),

    path('device-models/<int:pk>/firmware/create', DeviceModelFirmwareCreateView.as_view(), name='device_firmware_create'),
    path('device-models/<int:pk>/firmware/<int:fw_pk>/delete', DeviceModelFirmwareDeleteView.as_view(), name='device_firmware_delete'),
    path('device-models/<int:pk>/firmware/<int:fw_pk>/update', DeviceModelDetailView.as_view(), name='device_firmware_update'),

    path('chart/',  ChartView.as_view(), name='chart'),

]

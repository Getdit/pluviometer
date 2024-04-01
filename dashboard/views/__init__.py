from .map_view import MapView
from .alert import AlertListView, AlertCreateView, AlertUpdateView, AlertDeleteView, get_devices_params
from .device import DeviceListView, ProjectDeviceListView, ProjectDeviceAddView, ProjectDeviceRemoveView, DeviceLogsView, DeviceCreateView, DeviceUpdateView, DeviceDeleteView
from .device_model import DeviceModelListView, DeviceModelDetailView, DeviceModelCreateView, DeviceModelUpdateView, DeviceModelDeleteView, DeviceModelFirmwareCreateView, DeviceModelFirmwareDeleteView
from .project import ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectListView, ProjectChartFormView
from .project_user import ProjectUserListView, ProjectAssignUserView, ProjectUserRemoveView
from .data_model import DataModelCreateView, DataModelDeleteView, DataModelUpdateView
from .locations import LocationListView, LocationCreateView, LocationUpdateView, LocationDeleteView

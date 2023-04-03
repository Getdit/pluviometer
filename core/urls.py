from django.urls import path
from core.views import download_temporary_file, showFirebaseJS

app_name = "core"

urlpatterns = [
    path("download/<slug:uuid>/", download_temporary_file, name="download-temporary-file"),
    path("firebase-messaging-sw.js", showFirebaseJS, name="show-firebase-ja"),
]
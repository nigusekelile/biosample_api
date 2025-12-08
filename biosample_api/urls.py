from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/samples/", include("samples.urls")),
    path("api/qc/", include("qc.urls")),
    path("api/auth/", include("users.urls")),
]

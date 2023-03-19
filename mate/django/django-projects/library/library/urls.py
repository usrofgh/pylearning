from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("hello/<int:unique_number>/", hello_world)
    path("catalog/", include("catalog.urls", namespace="catalog"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


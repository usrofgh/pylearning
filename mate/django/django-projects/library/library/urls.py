from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    # path("hello/<int:unique_number>/", hello_world)
    path("catalog/", include("catalog.urls", namespace="catalog")),
    # path("accounts/", include("accounts.urls", namespace="account")),
    path("accounts/", include("django.contrib.auth.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    # Local apps
    path('accounts/', include('accounts.urls')),
    # Browser reload
    path("__reload__/", include("django_browser_reload.urls")),
]

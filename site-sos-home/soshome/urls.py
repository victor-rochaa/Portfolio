from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('api.urls')),
    path('services/', include('services.urls')),
]

# Direcionamento do erro 404
handler404 = "pages.views.handler404"
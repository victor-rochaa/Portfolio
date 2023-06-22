from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),
]

# Direcionamento do erro 404
handler404 = "blog.views.handler404"
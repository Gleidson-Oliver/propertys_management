from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from project.views import custom_logout_view

urlpatterns = [
    path('', include('Alugueis.urls')),
    path('admin/logout/', custom_logout_view, name='custom_logout_view'),  # Adicionando a nova URL de logout
    path("admin/", admin.site.urls),
    path('', include('admin_material.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

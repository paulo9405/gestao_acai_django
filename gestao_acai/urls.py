from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]

admin.site.site_header = 'Gestão Açai da Rose'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Seja bem vindo a Gestão Açai da Rose'

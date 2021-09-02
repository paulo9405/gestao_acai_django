from django.urls import path
from .views import DashboardView, VendaCreate, VendaLista


urlpatterns = [
    path('', DashboardView.as_view(), name="core_dashboard"),
    path('dashboard/', DashboardView.as_view(), name="core_dashboard"),
    path('venda_create/', VendaCreate.as_view(), name="core_venda_create"),
    path('venda_list/', VendaLista.as_view(), name="core_venda_lista"),
]

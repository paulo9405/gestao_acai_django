from django.urls import path
from .views import DashboardView, VendaCreate, VendaLista



urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name="core_dashboard"),
    #path('vendas-diaria-lista/', venda_diaria_lista, name="core_venda_diaria_lista"),
    #path('venda-nova/', venda_nova, name="core_venda_nova"),
    path('venda_create/', VendaCreate.as_view(), name="core_venda_create"),
    path('venda_list/', VendaLista.as_view(), name="core_venda_lista"),
]

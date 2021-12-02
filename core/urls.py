from django.urls import path
from .views import (
    DashboardView,
    VendaCreate,
    VendaLista,
    ColaboradorCreate,
    ColaboradoresLista,
    Vendas_pdf,
    Vendas_csv,
    api,
)


urlpatterns = [
    path('', DashboardView.as_view(), name="core_dashboard"),
    path('dashboard/', DashboardView.as_view(), name="core_dashboard"),
    path('venda_create/', VendaCreate.as_view(), name="core_venda_create"),
    path('venda_list/', VendaLista.as_view(), name="core_venda_lista"),

    path('colaborador_create/', ColaboradorCreate.as_view(),
         name="core_colaborador_create"),

    path('colaborador_list/', ColaboradoresLista.as_view(),
         name="core_colaboradores_list"),

    path('vendas-pdf/', Vendas_pdf.as_view(),
        name='core_vendas_pdf'),

    path('vendas-csv/', Vendas_csv.as_view(),
        name='core_vendas_csv'),

    path('api/', api, name="api"),

]

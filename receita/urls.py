from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import (
    ReceitaListarCriarView,
    ReceitaRetrieveUpdateDeleteView,
    CategoriaListarCriarView,
    CategoriaRetrieveUpdateDeleteView,
    InteracaoListarCriarView,
    InteracaoRetrieveDeleteView,
)

urlpatterns = [
    path('receitas/', ReceitaListarCriarView.as_view(), name='receita-listar-criar'),
    path('receitas/<int:pk>/', ReceitaRetrieveUpdateDeleteView.as_view(), name='receita-detalhe'),


    path('categorias/', CategoriaListarCriarView.as_view(), name='categoria-listar-criar'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDeleteView.as_view(), name='categoria-detalhe'),

    path('interacoes/', InteracaoListarCriarView.as_view(), name='interacao-listar-criar'),
    path('interacoes/<int:pk>/', InteracaoRetrieveDeleteView.as_view(), name='interacao-detalhe'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


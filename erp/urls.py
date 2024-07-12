from django.urls import path
from erp.views import criar_funcionario, listar_funcionarios, detalhe_funcionario, atualizar_funcionario, HomeView, \
    ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView, ProdutoDeleteView, VendaCreateView, \
    VendaListView, VendaDetailView, VendaUpdateView, VendaDeleteView, deletar_funcionario

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Funcionários
    path('funcionarios/', listar_funcionarios, name='listar_funcionarios'),
    path('funcionarios/novo', criar_funcionario, name='criar_funcionario'),
    path('funcionarios/detalhe/<pk>', detalhe_funcionario, name='detalhe_funcionario'),
    path('funcionarios/atualizar/<pk>', atualizar_funcionario, name='atualizar_funcionario'),
    path('funcionarios/deletar/<pk>', deletar_funcionario, name='deletar_funcionario'),
    # Produtos
    path('produtos/', ProdutoListView.as_view(), name='listar_produto'),
    path('produtos/novo', ProdutoCreateView.as_view(), name='cadastro_produto'),
    path('produtos/atualizar/<pk>', ProdutoUpdateView.as_view(), name='atualizar_produto'),
    path('produtos/detalhe/<pk>', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('produtos/deletar/<pk>', ProdutoDeleteView.as_view(), name='deletar_produto'),
    # Vendas
    path('vendas/', VendaListView.as_view(), name='listar_venda'),
    path('vendas/novo', VendaCreateView.as_view(), name='criar_venda'),
    path('vendas/detalhe/<pk>', VendaDetailView.as_view(), name='detalhe_venda'),
    path('vendas/atualizar/<pk>', VendaUpdateView.as_view(), name='atualizar_venda'),
    path('vendas/deletar/<pk>', VendaDeleteView.as_view(), name='deletar_venda'),
]

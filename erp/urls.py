from django.urls import path
from erp.views import criar_funcionario, listar_funcionarios, detalhe_funcionario, atualizar_funcionario, HomeView, \
    ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView, ProdutoDeleteView

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Funcionários
    path('funcionarios/novo', criar_funcionario, name='criar_funcionario'),
    path('funcionarios/listar', listar_funcionarios, name='listar_funcionarios'),
    path('funcionarios/detalhe/<pk>', detalhe_funcionario, name='detalhe_funcionario'),
    path('funcionarios/atualizar/<pk>', atualizar_funcionario, name='atualizar_funcionario'),
    # Produtos
    path('produtos/', ProdutoListView.as_view(), name='listar_produto'),
    path('produtos/novo', ProdutoCreateView.as_view(), name='cadastro_produto'),
    path('produtos/atualizar/<pk>', ProdutoUpdateView.as_view(), name='atualizar_produto'),
    path('produtos/detalhe/<pk>', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('produtos/deletar/<pk>', ProdutoDeleteView.as_view(), name='deletar_produto'),
]

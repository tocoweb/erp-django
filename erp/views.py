from django.contrib.messages import success
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse

from erp.forms import FuncionarioForm, ProdutoForm, VendaForm
from erp.models import Funcionario, Produto, Venda


class HomeView(TemplateView):
    template_name = 'erp/index.html'


def criar_funcionario(request: HttpRequest):
    if request.method == 'GET':
        form = FuncionarioForm()

        return render(request, template_name='erp/funcionarios/criar_funcionarios.html', context={'form': form})

    elif request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)
            funcionario.save()

            return HttpResponseRedirect(redirect_to='/funcionarios')


def listar_funcionarios(request: HttpRequest):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        qt_func = len(funcionarios)

    return render(request, template_name='erp/funcionarios/listar_funcionarios.html', context={
        'funcionarios': funcionarios,
        'qt_func': qt_func,
    })


def detalhe_funcionario(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None

        return render(request, template_name='erp/funcionarios/detalhe_funcionario.html', context={'funcionario': funcionario})


def deletar_funcionario(request: HttpRequest, pk: int):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    print(funcionario)

    if request.method == 'POST':
        funcionario.delete()
        return HttpResponseRedirect(redirect_to='/funcionarios')

    return render(request, template_name='erp/funcionarios/deletar_funcionario.html', context={'funcionario': funcionario})


def atualizar_funcionario(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
            form = FuncionarioForm(instance=funcionario)

            return render(request, template_name='erp/funcionarios/editar_funcionario.html', context={'form': form, 'funcionario': funcionario})
        except Funcionario.DoesNotExist:
            funcionario = None

    elif request.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'erp/produtos/novo.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'erp/produtos/listar.html'
    context_object_name = 'produtos'


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'erp/produtos/atualizar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:listar_produto')


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'erp/produtos/detalhe.html'
    context_object_name = 'produto'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'erp/produtos/deletar.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('erp:listar_produto')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaCreateView(CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:listar_venda')
    fields = ['funcionario', 'produto']


class VendaListView(ListView):
    model = Venda
    template_name = 'erp/vendas/listar.html'
    context_object_name = 'vendas'


class VendaDetailView(DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualizar.html'
    form_class = VendaForm
    success_url = reverse_lazy('erp:listar_venda')


class VendaDeleteView(DeleteView):
    model = Venda
    template_name = 'erp/vendas/deletar.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:listar_venda')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
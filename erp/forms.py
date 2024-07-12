from django import forms

from erp.models import Funcionario, Produto, Venda


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'email_funcional',
            'remuneracao'
        ]


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        labels = {
            'descricao': 'Descrição',
            'preco': 'Preço',
        }


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['funcionario', 'produto']
        labels = {
            'funcionario': 'Funcionário',
        }

from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    sobrenome = models.CharField(max_length=70, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    email_funcional = models.EmailField(max_length=50, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)


class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)


class Venda(models.Model):
    funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)


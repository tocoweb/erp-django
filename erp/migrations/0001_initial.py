# Generated by Django 4.2.7 on 2023-11-29 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=70)),
                ('cpf', models.CharField(max_length=14)),
                ('email_funcional', models.EmailField(max_length=50)),
                ('remuneracao', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.funcionario')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.produto')),
            ],
        ),
    ]

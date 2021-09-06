# Generated by Django 3.2.6 on 2021-09-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_venda_dia_da_venda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('endereço', models.CharField(max_length=200)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descricao_salario', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
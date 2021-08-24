# Generated by Django 3.2.6 on 2021-08-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_vendadiaria_despesa_do_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendadiaria',
            name='despesa_do_dia',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vendadiaria',
            name='lucro_liquido',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vendadiaria',
            name='venda_total_dia',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
    ]

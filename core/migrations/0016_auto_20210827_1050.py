# Generated by Django 3.2.6 on 2021-08-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210827_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='compras',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='venda',
            name='despesas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

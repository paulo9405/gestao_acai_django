# Generated by Django 3.2.6 on 2021-08-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_vendadiaria_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntregaMes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='vendadiaria',
            name='lucro_liquido',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

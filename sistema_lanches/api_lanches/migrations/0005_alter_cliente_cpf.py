# Generated by Django 5.1.6 on 2025-02-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lanches', '0004_alter_cliente_cpf_alter_pedido_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

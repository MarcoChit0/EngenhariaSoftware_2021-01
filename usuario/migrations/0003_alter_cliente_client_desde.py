# Generated by Django 4.0.3 on 2022-04-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_cliente_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='client_desde',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Cliente desde'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-27 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaoDeCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=16)),
                ('saldo', models.IntegerField(default=0)),
                ('validade', models.IntegerField(default=0)),
                ('cvv', models.CharField(max_length=3)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(default=0)),
                ('cartao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagamento.cartaodecredito')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.cliente')),
            ],
        ),
    ]
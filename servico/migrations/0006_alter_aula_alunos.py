# Generated by Django 4.0.3 on 2022-04-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('servico', '0005_remove_aula_cliente_aula_alunos_aula_max_alunos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(blank=True, max_length=models.IntegerField(), to='usuario.cliente'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-29 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('servico', '0003_alter_consulta_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.cliente'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.cliente'),
        ),
    ]

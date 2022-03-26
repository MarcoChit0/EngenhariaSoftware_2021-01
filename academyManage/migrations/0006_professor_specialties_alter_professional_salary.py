# Generated by Django 4.0.3 on 2022-03-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyManage', '0005_remove_professor_specialties'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='specialties',
            field=models.CharField(choices=[('NAS', 'None'), ('SUPINO DE 20', 'Supino de 20'), ('CROSSFIT', 'Crossfit')], default='NAS', max_length=32),
        ),
        migrations.AlterField(
            model_name='professional',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]

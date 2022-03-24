# Generated by Django 4.0.3 on 2022-03-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32)),
                ('client_since', models.DateTimeField(verbose_name='Client Since')),
            ],
        ),
    ]

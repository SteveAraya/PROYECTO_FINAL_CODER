# Generated by Django 4.0.6 on 2022-08-20 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=50)),
                ('annio', models.IntegerField()),
                ('tipo_caja', models.CharField(max_length=50)),
                ('combustible', models.CharField(max_length=50)),
                ('cantidad_pasajeros', models.IntegerField()),
                ('numero_puertas', models.IntegerField()),
            ],
        ),
    ]
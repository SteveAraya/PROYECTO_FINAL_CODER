# Generated by Django 4.0.6 on 2022-08-24 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ubicacion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=200)),
            ],
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0003_categoria_remove_post_categoria_post_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Register', '0002_avatar_delete_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, default=1, upload_to='avatares'),
            preserve_default=False,
        ),
    ]

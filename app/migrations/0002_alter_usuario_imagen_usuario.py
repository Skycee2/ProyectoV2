# Generated by Django 4.0.4 on 2022-05-16 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen_usuario',
            field=models.ImageField(null=True, upload_to='usuarios'),
        ),
    ]

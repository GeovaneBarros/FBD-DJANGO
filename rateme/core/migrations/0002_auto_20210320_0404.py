# Generated by Django 3.1.7 on 2021-03-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nome_usuario',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
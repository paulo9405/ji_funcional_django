# Generated by Django 3.2.4 on 2021-06-12 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210611_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichapessoa',
            name='data_inicio',
            field=models.DateField(verbose_name='Data do inicio das atividades'),
        ),
    ]

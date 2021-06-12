# Generated by Django 3.2.4 on 2021-06-12 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_fichapessoa_data_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='data_nascimento',
        ),
        migrations.AlterField(
            model_name='fichapessoa',
            name='data_inicio',
            field=models.DateTimeField(verbose_name='Inicio das atividades'),
        ),
    ]

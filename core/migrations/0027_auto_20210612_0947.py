# Generated by Django 3.2.4 on 2021-06-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_remove_pessoa_horario_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='horario_registro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ultima_vez_modificado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

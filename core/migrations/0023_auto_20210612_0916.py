# Generated by Django 3.2.4 on 2021-06-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_fichapessoa_peso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='endereço',
            new_name='endereco',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='meu_campo_obrigatorio',
            field=models.CharField(default='Meu valor default', max_length=100),
        ),
    ]

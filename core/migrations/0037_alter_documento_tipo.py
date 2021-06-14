# Generated by Django 3.2.4 on 2021-06-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_endereco_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='tipo',
            field=models.CharField(choices=[('RG', 'Carteira de Identidade (RG)'), ('CPF', 'Cadastro Unico de Pessoa Fisica (CPF)'), ('PP', 'Passaporte')], max_length=3),
        ),
    ]
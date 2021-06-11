# Generated by Django 3.2.4 on 2021-06-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('endereço', models.CharField(max_length=100, verbose_name='Endereço')),
                ('plano_mes', models.BooleanField(default=False, verbose_name='Plano Mensal R$ 50,00')),
                ('plano_tri', models.BooleanField(default=False, verbose_name='Plano Trimestral R$ 130,00')),
            ],
        ),
    ]

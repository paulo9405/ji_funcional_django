# Generated by Django 3.2.4 on 2021-06-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
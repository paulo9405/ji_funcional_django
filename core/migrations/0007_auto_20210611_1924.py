# Generated by Django 3.2.4 on 2021-06-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210611_1920'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Parametros',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='plano_mes',
            field=models.BooleanField(null=True, verbose_name='Plano Mensal R$ 50,00'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='plano_tri',
            field=models.BooleanField(null=True, verbose_name='Plano Trimestral R$ 130,00'),
        ),
    ]

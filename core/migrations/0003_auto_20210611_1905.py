# Generated by Django 3.2.4 on 2021-06-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pessoa_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(default=1, max_length=100, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='plano_mes',
            field=models.BooleanField(default=False, null=True, verbose_name='Plano Mensal R$ 50,00'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='plano_tri',
            field=models.BooleanField(default=False, null=True, verbose_name='Plano Trimestral R$ 130,00'),
        ),
    ]
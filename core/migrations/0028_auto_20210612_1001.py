# Generated by Django 3.2.4 on 2021-06-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20210612_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='plano',
        ),
    ]

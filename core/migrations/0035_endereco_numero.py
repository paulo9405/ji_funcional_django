# Generated by Django 3.2.4 on 2021-06-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20210612_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(max_length=6, null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-11 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_fichapessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichapessoa',
            name='altura',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='fichapessoa',
            name='imc',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='fichapessoa',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]

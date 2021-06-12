# Generated by Django 3.2.4 on 2021-06-12 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_pessoa_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='endereco',
        ),
        migrations.AddField(
            model_name='endereco',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pessoa'),
        ),
    ]

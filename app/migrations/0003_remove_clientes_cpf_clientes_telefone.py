# Generated by Django 4.2.1 on 2023-06-01 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_clientes_fk_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='cpf',
        ),
        migrations.AddField(
            model_name='clientes',
            name='telefone',
            field=models.BigIntegerField(default=11),
            preserve_default=False,
        ),
    ]

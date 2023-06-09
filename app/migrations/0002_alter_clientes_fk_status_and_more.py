# Generated by Django 4.2.2 on 2023-06-21 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='fk_status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='estacionamento',
            name='fk_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='estacionamento',
            name='fk_veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.veiculos', verbose_name='Veiculo'),
        ),
        migrations.AlterField(
            model_name='marcas',
            name='fk_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='mensalidades',
            name='fk_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientes', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='modelos',
            name='fk_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.marcas', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='modelos',
            name='fk_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='modelos',
            name='fk_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipos', verbose_name='Tipo de Veiculo'),
        ),
        migrations.AlterField(
            model_name='precos',
            name='fk_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='precos',
            name='fk_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipos', verbose_name='Tipo de Veiculo'),
        ),
        migrations.AlterField(
            model_name='precos',
            name='por_hora',
            field=models.DecimalField(decimal_places=4, max_digits=11, verbose_name='Preço por hora'),
        ),
        migrations.AlterField(
            model_name='precos',
            name='por_mensalidade',
            field=models.DecimalField(decimal_places=4, max_digits=11, verbose_name='Preço por mensalidade'),
        ),
        migrations.AlterField(
            model_name='registros',
            name='fk_status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='registros',
            name='fk_tipoRegistro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tiposregistros', verbose_name='Tipo de Registro'),
        ),
        migrations.AlterField(
            model_name='registros',
            name='fk_veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.veiculos', verbose_name='Veiculo'),
        ),
        migrations.AlterField(
            model_name='tipos',
            name='fk_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='veiculos',
            name='fk_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.clientes', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='veiculos',
            name='fk_modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.modelos', verbose_name='Modelo de Veiculo'),
        ),
        migrations.AlterField(
            model_name='veiculos',
            name='fk_status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Status'),
        ),
    ]

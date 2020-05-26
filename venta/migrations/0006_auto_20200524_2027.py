# Generated by Django 3.0.6 on 2020-05-25 00:27

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0005_auto_20200524_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=django_fsm.FSMField(choices=[(0, 'creada'), (1, 'cagada'), (2, 'facturada'), (3, 'finalizada'), (4, 'cancelada'), (5, 'anulada')], default='creada', max_length=50, protected=True),
        ),
    ]

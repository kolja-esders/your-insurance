# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171008_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='nb_con1',
        ),
        migrations.AddField(
            model_name='person',
            name='nb_con1',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nb_conn1', to='core.Contract'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='person',
            name='nb_con2',
        ),
        migrations.AddField(
            model_name='person',
            name='nb_con2',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nb_conn2', to='core.Contract'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='person',
            name='nb_con3',
        ),
        migrations.AddField(
            model_name='person',
            name='nb_con3',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nb_conn3', to='core.Contract'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='person',
            name='nb_con4',
        ),
        migrations.AddField(
            model_name='person',
            name='nb_con4',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nb_conn4', to='core.Contract'),
            preserve_default=False,
        ),
    ]
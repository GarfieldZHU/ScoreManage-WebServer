# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='clsid',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='student',
            name='sid',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='grade',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tid',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tpwd',
            field=models.CharField(max_length=15),
        ),
    ]

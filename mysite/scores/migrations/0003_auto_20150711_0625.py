# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_auto_20150711_0605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcourse',
            name='teacher',
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='course',
            field=models.ForeignKey(default=' ', to='scores.Course'),
            preserve_default=False,
        ),
    ]

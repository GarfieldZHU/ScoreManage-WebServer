# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0003_auto_20150711_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cname',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]

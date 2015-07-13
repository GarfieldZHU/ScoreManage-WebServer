# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('clsid', models.CharField(max_length=5, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('credit', models.IntegerField(default=0)),
                ('semester', models.CharField(max_length=2)),
                ('period', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('sname', models.CharField(max_length=10)),
                ('spwd', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=4)),
                ('age', models.IntegerField(default=18)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=3)),
                ('student', models.ForeignKey(to='scores.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('tname', models.CharField(max_length=10)),
                ('tpwd', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=4)),
                ('workage', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='teacher',
            field=models.ForeignKey(to='scores.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='scores.Teacher'),
        ),
    ]

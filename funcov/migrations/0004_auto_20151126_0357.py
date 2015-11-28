# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0003_coverpoint_enable'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverpoint',
            name='covergroup',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='coverpoint',
            name='desc',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='coverpoint',
            name='expr',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='coverpoint',
            name='owner',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='coverpoint',
            name='sensitivityLabel',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='coverpoint',
            name='type',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='name',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]

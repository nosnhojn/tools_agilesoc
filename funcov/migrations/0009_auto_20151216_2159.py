# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0008_auto_20151210_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='covergroup',
            name='beginning',
            field=models.CharField(default=b'', max_length=10000),
        ),
        migrations.AddField(
            model_name='covergroup',
            name='middle',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]

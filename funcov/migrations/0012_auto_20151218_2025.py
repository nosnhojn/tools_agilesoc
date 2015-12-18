# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0011_auto_20151218_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverpoint',
            name='desc',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]

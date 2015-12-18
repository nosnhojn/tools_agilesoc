# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0009_auto_20151216_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='covergroup',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]

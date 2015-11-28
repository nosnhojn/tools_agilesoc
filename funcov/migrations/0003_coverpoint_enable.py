# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0002_coverpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverpoint',
            name='enable',
            field=models.BooleanField(default=True),
        ),
    ]

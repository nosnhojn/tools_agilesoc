# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0006_covergroup_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverpoint',
            name='sensitivity',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]

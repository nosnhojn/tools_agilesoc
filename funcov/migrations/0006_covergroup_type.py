# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0005_covergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='covergroup',
            name='type',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]

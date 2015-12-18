# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0010_covergroup_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverpoint',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='coverpoint',
            name='type',
        ),
        migrations.RemoveField(
            model_name='parameter',
            name='owner',
        ),
        migrations.AddField(
            model_name='covergroup',
            name='owner',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='coverpoint',
            name='kind',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='covergroup',
            name='name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='covergroup',
            name='type',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='covergroup',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='desc',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='expr',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='sensitivity',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='sensitivityLabel',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='covergroup',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='parameterchoice',
            name='choice',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='parameterchoice',
            name='param',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]

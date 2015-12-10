# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcov', '0007_coverpoint_sensitivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable', models.BooleanField(default=True)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('owner', models.CharField(default=b'', max_length=128)),
                ('covergroup', models.CharField(default=b'', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ParameterChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('param', models.CharField(default=b'', max_length=128)),
                ('choice', models.CharField(default=b'', max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='coverpoint',
            name='sensitivity',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='parameter',
            name='select',
            field=models.ForeignKey(blank=True, to='funcov.ParameterChoice', null=True),
        ),
    ]

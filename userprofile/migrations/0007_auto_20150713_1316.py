# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20150704_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rank',
            field=models.CharField(default=b'LR', max_length=3, choices=[(b'LR', b'Low Rank'), (b'HR', b'High Rank'), (b'GR', b'G-Rank'), (b'GRP', b'G-Rank 100-998'), (b'GM', b'G-Rank 999')]),
        ),
    ]

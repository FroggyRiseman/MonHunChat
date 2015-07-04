# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20150704_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rank',
            field=models.CharField(default=b'hr1', max_length=3, choices=[(b'hr1', b'HR1'), (b'hr2', b'HR2'), (b'hr3', b'HR3'), (b'hr4', b'HR4'), (b'hr5', b'HR5'), (b'hr6', b'HR6'), (b'hr7', b'HR7'), (b'hr8', b'HR8'), (b'hr9', b'HR9')]),
            preserve_default=True,
        ),
    ]

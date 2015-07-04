# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofile_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rank',
            field=models.CharField(default=b'LR1', max_length=2, choices=[(b'LR1', b'1'), (b'LR2', b'2'), (b'LR3', b'3'), (b'HR4', b'4'), (b'HR5', b'5'), (b'HR6', b'6'), (b'HR7', b'7'), (b'G8', b'8'), (b'G9', b'9')]),
            preserve_default=True,
        ),
    ]

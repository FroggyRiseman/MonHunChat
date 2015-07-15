# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_auto_20150715_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='fc',
            new_name='friend_code',
        ),
    ]

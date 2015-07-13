# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20150713_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favorite_weapon',
            new_name='weapon',
        ),
    ]

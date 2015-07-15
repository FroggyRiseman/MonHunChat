# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_auto_20150715_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hunter_name',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nintendo_name',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skype_name',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='teamspeak_name',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
    ]

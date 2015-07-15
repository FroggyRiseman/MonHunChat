# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_auto_20150713_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fc',
            field=models.CharField(default=b'', help_text=b'Please use the following format: <em>####-####-####</em>.', max_length=14, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weapon',
            field=models.CharField(default=None, max_length=3, null=True, blank=True, choices=[(b'GS', b'Greatsword'), (b'LS', b'Longsword'), (b'SNS', b'Sword & Shield'), (b'DB', b'Dual Blades'), (b'HAM', b'Hammer'), (b'HH', b'Hunting Horn'), (b'LAN', b'Lance'), (b'GL', b'Gunlance'), (b'SA', b'Switch Axe'), (b'CA', b'Charge Axe'), (b'IG', b'Insect Glaive'), (b'TON', b'Tonfa'), (b'BOW', b'Bow'), (b'HBG', b'Heavy Bowgun'), (b'LBG', b'Light Bowgun')]),
        ),
    ]

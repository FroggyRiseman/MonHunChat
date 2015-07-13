# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_remove_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorite_weapon',
            field=models.CharField(default=None, max_length=3, choices=[(b'GS', b'Greatsword'), (b'LS', b'Longsword'), (b'SNS', b'Sword & Shield'), (b'DB', b'Dual Blades'), (b'HAM', b'Hammer'), (b'HH', b'Hunting Horn'), (b'LAN', b'Lance'), (b'GL', b'Gunlance'), (b'SA', b'Switch Axe'), (b'CA', b'Charge Axe'), (b'IG', b'Insect Glaive'), (b'TON', b'Tonfa'), (b'BOW', b'Bow'), (b'HBG', b'Heavy Bowgun'), (b'LBG', b'Light Bowgun')]),
        ),
    ]

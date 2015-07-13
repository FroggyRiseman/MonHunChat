# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_userprofile_favorite_weapon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_weapon',
            field=models.CharField(max_length=3, null=True, choices=[(b'GS', b'Greatsword'), (b'LS', b'Longsword'), (b'SNS', b'Sword & Shield'), (b'DB', b'Dual Blades'), (b'HAM', b'Hammer'), (b'HH', b'Hunting Horn'), (b'LAN', b'Lance'), (b'GL', b'Gunlance'), (b'SA', b'Switch Axe'), (b'CA', b'Charge Axe'), (b'IG', b'Insect Glaive'), (b'TON', b'Tonfa'), (b'BOW', b'Bow'), (b'HBG', b'Heavy Bowgun'), (b'LBG', b'Light Bowgun')]),
        ),
    ]

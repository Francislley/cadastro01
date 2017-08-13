# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contacts',
            field=models.ManyToManyField(related_name='_contacts_+', to='profiles.Profile'),
        ),
    ]

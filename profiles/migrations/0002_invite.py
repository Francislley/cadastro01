# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('invited', models.ForeignKey(related_name='invitations_received', to='profiles.Profile')),
                ('requester', models.ForeignKey(related_name='invitations_made', to='profiles.Profile')),
            ],
        ),
    ]

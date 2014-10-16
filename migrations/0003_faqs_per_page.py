# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_auto_20141010_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqs',
            name='per_page',
            field=models.IntegerField(default=5, null=True, verbose_name=b'faqs per page', blank=True),
            preserve_default=True,
        ),
    ]

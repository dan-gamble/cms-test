# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqs',
            name='footer_text',
        ),
        migrations.RemoveField(
            model_name='faqs',
            name='header_text',
        ),
        migrations.AddField(
            model_name='faqs',
            name='standfirst',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

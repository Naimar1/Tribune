# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 16:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_newsletterrecipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]

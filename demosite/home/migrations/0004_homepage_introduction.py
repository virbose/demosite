# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 18:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='introduction',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=250),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 17:38
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0013_remove_certificategenerationcoursesetting_enabled'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='generatedcertificate',
            managers=[
                ('eligible_certificates', django.db.models.manager.Manager()),
            ],
        ),
    ]

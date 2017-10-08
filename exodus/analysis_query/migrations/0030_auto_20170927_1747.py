# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 17:47
from __future__ import unicode_literals

import analysis_query.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0029_auto_20170925_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='handle',
            field=models.CharField(max_length=500, validators=[analysis_query.models.validate_handle]),
        ),
        migrations.AlterField(
            model_name='analysisrequest',
            name='storage_path',
            field=models.TextField(default=b'/home/lambda/Make/Exodus/exodus/storage/apks/dzylwaguxnkqgushhnidcidvwyxhpgilyvqdexupnrrntwufvsvfvqvibtbjcxux'),
        ),
        migrations.AlterField(
            model_name='analysisrequest',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BowlGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bowl', models.CharField(max_length=150)),
                ('fav', models.CharField(max_length=150)),
                ('dog', models.CharField(max_length=150)),
                ('hilo', models.IntegerField()),
                ('spread', models.IntegerField()),
            ],
        ),
    ]

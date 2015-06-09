# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bowlgame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

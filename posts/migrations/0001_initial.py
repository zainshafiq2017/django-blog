# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, null=True, default=django.utils.timezone.now)),
                ('views', models.IntegerField(default=0)),
                ('tag', models.CharField(max_length=30, blank=True, null=True)),
                ('image', models.ImageField(upload_to='img', blank=True, null=True)),
            ],
        ),
    ]

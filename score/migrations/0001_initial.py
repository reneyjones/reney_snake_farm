# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 14:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('player1_name', models.CharField(max_length=50)),
                ('player1_score', models.IntegerField()),
                ('player2_name', models.CharField(max_length=50)),
                ('player2_score', models.IntegerField()),
                ('player3_name', models.CharField(max_length=50)),
                ('player3_score', models.IntegerField()),
                ('player4_name', models.CharField(max_length=50)),
                ('player4_score', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

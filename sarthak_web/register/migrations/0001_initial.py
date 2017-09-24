# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 13:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=120)),
                ('Mobile_number', models.IntegerField(unique=True)),
                ('Address', models.CharField(max_length=10000)),
                ('College', models.CharField(max_length=500)),
                ('IEEE_mem_no', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
            ],
        ),
    ]
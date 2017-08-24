# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
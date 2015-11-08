# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True, help_text='')),
                ('name', models.CharField(max_length=100, help_text='')),
                ('due_date', models.DateTimeField(help_text='')),
            ],
        ),
        migrations.CreateModel(
            name='ChoreList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True, help_text='')),
                ('name', models.CharField(max_length=100, help_text='')),
                ('due_date', models.DateTimeField(help_text='')),
            ],
        ),
        migrations.AddField(
            model_name='chore',
            name='chore_list',
            field=models.ForeignKey(to='chores.ChoreList', help_text=''),
        ),
    ]

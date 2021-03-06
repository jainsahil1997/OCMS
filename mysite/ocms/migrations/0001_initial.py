# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-15 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('dd_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('complaint_desc', models.CharField(default='code', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Property_Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('property_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocms.Property')),
            ],
        ),
        migrations.AddField(
            model_name='complaint_type',
            name='dept_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocms.Department'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_type',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='dept_name', chained_model_field='dept_name', on_delete=django.db.models.deletion.CASCADE, to='ocms.Complaint_Type'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='dept_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocms.Department'),
        ),
    ]

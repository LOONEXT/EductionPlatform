# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-14 10:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Course Name')),
                ('desc', models.CharField(max_length=300, verbose_name='Course Introduction')),
                ('detail', models.TextField(verbose_name='Course Detail Description')),
                ('degree', models.CharField(choices=[('cj', 'primary'), ('zj', 'intermediate'), ('gj', 'advanced')], max_length=30)),
                ('learn_times', models.IntegerField(default=0, verbose_name='Learn Times')),
                ('students', models.IntegerField(default=0, verbose_name='Learn Students')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Collection Students')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='Upload Image')),
                ('click_nums', models.IntegerField(default=0, verbose_name='Click Number')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Course',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='Download')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add Time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Course Resource',
                'verbose_name_plural': 'Course Resource',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Lesson Name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add Time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lesson',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Viedo Name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add Time')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='Lession')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
            },
        ),
    ]
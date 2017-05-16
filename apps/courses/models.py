# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class Course(models.Model):
    """课程表"""
    # 课程名称
    name = models.CharField(max_length=50, verbose_name=_('Course Name'))
    desc = models.CharField(max_length=300, verbose_name=_('Course Introduction'))
    # 课程详情
    detail = models.TextField(verbose_name=_('Course Detail Description'))
    # 课程等级
    degree = models.CharField(max_length=30,
                              choices=(('cj', _('primary')), ('zj', _('intermediate')), ('gj', _('advanced'))))
    learn_times = models.IntegerField(default=0, verbose_name=_('Learn Times'))
    students = models.IntegerField(default=0, verbose_name=_('Learn Students'))
    # 收藏人数
    fav_nums = models.IntegerField(default=0, verbose_name=_('Collection Students'))
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=_('Upload Image'))
    click_nums = models.IntegerField(default=0, verbose_name=_('Click Number'))
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    """章节表"""
    course = models.ForeignKey(Course, verbose_name=_('Course'))
    name = models.CharField(max_length=100, verbose_name=_('Lesson Name'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = verbose_name

class Video(models.Model):
    """视频表"""
    lesson = models.ForeignKey(Lesson, verbose_name=_('Lession'))
    name = models.CharField(max_length=100, verbose_name=_('Viedo Name'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = verbose_name

class CourseResource(models.Model):
    """资源下载表"""
    course = models.ForeignKey(Course, verbose_name=_('Course'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=_('Download'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('Course Resource')
        verbose_name_plural = verbose_name


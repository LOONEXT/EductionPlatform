# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _

from users.models import UserProfile
from courses.models import Course

# Create your models here.
class UserAsk(models.Model):
    """用户咨询表"""
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    mobile = models.CharField(max_length=11, verbose_name=_('Mobile'))
    course_name = models.CharField(max_length=50, verbose_name=_('Course Name'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('User Ask')
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    """用户课程评论表"""
    user = models.ForeignKey(UserProfile, verbose_name=_('User'))
    course = models.ForeignKey(Course, verbose_name=_('Course'))
    comments = models.TextField(verbose_name=_('Comments'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('User Comment')
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """用户收藏"""
    user = models.ForeignKey(UserProfile, verbose_name=_('User'))
    fav_id = models.IntegerField(default=0, verbose_name=_('Favorite'))
    fav_type = models.IntegerField(
        choices=((1, _('Course Favorite')), (2, _('Teacher Favorite')), (3, _('Orgination Favorite'))), verbose_name=_('Favorite Type'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('User Favorite')
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """用户消息提醒"""
    user = models.IntegerField(default=0, verbose_name=_('Users'))
    message = models.CharField(max_length=200, verbose_name=_('User Message'))
    is_read = models.BooleanField(default=False, verbose_name=_('Is Read'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('User Message')
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """用户课程"""
    user = models.ForeignKey(UserProfile, verbose_name=_('User'))
    course = models.ForeignKey(Course, verbose_name=_('Course'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('User Course')
        verbose_name_plural = verbose_name

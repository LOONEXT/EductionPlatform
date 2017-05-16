# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class City(models.Model):
    """城市表"""
    name = models.CharField(max_length=20, verbose_name=_('City'))
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = verbose_name

class CourseOrg(models.Model):
    """课程机构表"""
    name = models.CharField(max_length=50, verbose_name=_('Orgnazition Name'))
    desc = models.TextField(verbose_name=_('Orgnazition Description'))
    click_nums = models.IntegerField(default=0, verbose_name=_('Click Numbers'))
    fav_nums = models.IntegerField(default=0, verbose_name=_('Fav number'))
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=_('Image'))
    address = models.CharField(max_length=150, verbose_name="Address")
    city = models.ForeignKey(City, verbose_name=_('City'))
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Orgnazition Info')
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    """教师表"""
    org = models.ForeignKey(CourseOrg, verbose_name=_('CourseOrg'))
    name = models.CharField(max_length=50, verbose_name=_('Teacher Name'))
    work_years = models.IntegerField(default=0, verbose_name=_('Work Years'))
    work_company = models.CharField(max_length=50, verbose_name=_('Work Company'))
    work_postion = models.CharField(max_length=50, verbose_name=_('Work Postion'))
    # 教学特点
    points = models.CharField(max_length=50, verbose_name=_('Points'))
    click_nums = models.IntegerField(default=0, verbose_name=_('Click Numbers'))
    fav_nums = models.IntegerField(default=0, verbose_name=_('Fav number'))
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Teacher Info')
        verbose_name_plural = verbose_name

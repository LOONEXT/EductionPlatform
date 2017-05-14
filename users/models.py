# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _

from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser): # AbstractUser 作为一个抽象基类`abstract=True`
    nick_name = models.CharField(max_length=50, verbose_name=_('Nick Name'))
    birthday = models.DateField(verbose_name=_('Birthday'), null=True, blank=True)
    gender = models.CharField(max_length=20, default='male',
                              choices=(('male', _('Male')), ('female', _('Female'))))
    address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default="image/default.png")

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = _('User Message')
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    """邮箱注册、找回密码生成邮箱验证码"""
    code = models.CharField(max_length=20, verbose_name=_('Verification Code'))
    email = models.EmailField(max_length=50, verbose_name=_('Email'))
    send_type = models.CharField(max_length=10, choices=(('register', _('Register')), ('forget', _('Forget Password'))))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Email Verification Code')
        verbose_name_plural = verbose_name


class Banner(models.Model):
    """首页轮播图数据库模型"""
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=_('Image'))
    url = models.URLField(max_length=200, verbose_name=_('Enter URL'))
    # 轮播图位置顺序
    index = models.IntegerField(default=100, verbose_name=_('order'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=_('Add Time'))

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = verbose_name

# -*- coding:utf-8 -*-
from __future__ import unicode_literals

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

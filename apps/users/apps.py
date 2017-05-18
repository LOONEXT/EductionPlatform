# -*- coding:utf-8 -*-
from django.utils.translation import ugettext as _
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = _('Users Information')

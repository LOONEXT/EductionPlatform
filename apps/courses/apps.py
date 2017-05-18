# -*- coding:utf-8 -*-
from django.utils.translation import ugettext as _
from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'courses'
    verbose_name = _('Course Information')

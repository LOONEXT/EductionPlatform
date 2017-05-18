# -*- coding:utf-8 -*-
from django.utils.translation import ugettext as _
from django.apps import AppConfig


class OrganizationConfig(AppConfig):
    name = 'organization'
    verbose_name = _('Organization Information')

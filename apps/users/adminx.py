#!/usr/bin/env python
# encoding: utf-8

import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

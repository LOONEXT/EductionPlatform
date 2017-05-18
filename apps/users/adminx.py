#!/usr/bin/env python
# encoding: utf-8

import xadmin

from .models import UserProfile, EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    # list页面要显示的字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # list页面添加搜索框
    search_fields = ['code', 'email', 'send_type']
    # list页面字段过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # list页面要显示的字段
    list_display = ['title', 'url', 'index', 'add_time']
    # list页面添加搜索框
    search_fields = ['title', 'url', 'index']
    # list页面字段过滤
    list_filter = ['title']



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


# 全局配置
class BaseSetting(object):
    # 主题设置
    enable_themes = True
    use_bootswatch = True


# 界面标题页脚设置
class GlobalSettings(object):
    site_title = u"慕学后台管理"
    site_footer = u"慕学在线网"
    # 菜单折叠
    menu_style = "accordion"


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
# 注册主题全局修改等功能到后台
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

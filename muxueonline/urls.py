# -*- coding: utf-8 -*-
"""muxueonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin

# from users import views
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, \
    ResetPwdView, ModifyPwdView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 验证码设置
    url(r'^captcha/', include('captcha.urls'), name='captcha'),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # 登录
    url(r'^login/$', LoginView.as_view(), name='login'),
    # 注册
    url(r'^register/$', RegisterView.as_view(), name='register'),
    # 注册激活码
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active'),
    # 重设密码激活码
    url(r'^forget/$', ForgetPwdView.as_view(), name='forgetpwd'),
    url(r'^resetpwd/(?P<active_code>.*)/$', ResetPwdView.as_view(), name='resetpwd'),
    url(r'^modifypwd/$', ModifyPwdView.as_view(), name='modifypwd'),
]

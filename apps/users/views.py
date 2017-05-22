# -*- coding:utf-8 -*-

# django用户登录验证
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
# 完成并集操作
from django.db.models import Q

from .models import UserProfile


# 修改authenticate方法自定义登录方式
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 利用username or email登录, 并集查询
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def sign_in(request):
    if request.method == "POST":
        # 取前端提交的数据
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 验证用户名和密码,需指定参数名称
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        return render(request, 'login.html', {'msg': u'用户名或密码错误'})
    elif request.method == "GET":
        return render(request, "login.html", {})

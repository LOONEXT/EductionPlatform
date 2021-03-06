# -*- coding:utf-8 -*-

# django用户登录验证
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
# 加密密码
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
# 完成并集操作
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from operations.models import UserMessage
from utils.email_send import send_register_email


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


# 类视图定义法
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        # 验证成功
        if login_form.is_valid():
            # 取前端提交的数据
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            # 验证用户名和密码,需指定参数名称
            user = authenticate(username=user_name, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                return render(request, 'login.html', {'msg': u'用户未激活!'})
            return render(request, 'index.html', {'msg': u'用户名或密码错误'})
        return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'register_form': register_form, 'msg': u'该邮箱已被注册！'})
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()

            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = u'欢迎注册慕学网！'
            user_message.save()

            send_register_email(email, 'register')
            return render(request, 'login.html')
        return render(request, 'register.html', {'register_form': register_form})


# 激活邮箱视图
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = all_records.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'login.html')
        return render(request, 'active_fail.html')


# 忘记密码视图
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetPwdView(View):
    def get(self, request, active_code):
        # 第二次点击链接处置 TODO
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
            return render(request, 'password_reset.html', {'emial': email})
        return render(request, 'active_fail.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm()
        email = request.POST.get('email', '')
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'modify_form': modify_form, 'msg': u'密码不一致！'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'password_reset.html', {'modify_form': modify_form, 'email': email})





# 函数视图定义法
# def sign_in(request):
    # if request.method == "POST":
        # # 取前端提交的数据
        # user_name = request.POST.get('username', '')
        # password = request.POST.get('password', '')
        # # 验证用户名和密码,需指定参数名称
        # user = authenticate(username=user_name, password=password)
        # if user is not None:
            # login(request, user)
            # return render(request, 'index.html')
        # return render(request, 'login.html', {'msg': u'用户名或密码错误'})
    # elif request.method == "GET":
        # return render(request, "login.html", {})

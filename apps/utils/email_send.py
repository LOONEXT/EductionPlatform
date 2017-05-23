# -*- coding:utf-8 -*-

from random import randint
import string

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from muxueonline.settings import EMAIL_FROM

def send_register_email(email, send_type="register"):
    code = random_str(16)
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = u"慕学网注册激活链接"
        email_body = u"请点击以下链接进行激活你的账号: http://127.0.0.1:8000/active/{}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status:
            # TODO
            print u"发送成功！"

    elif send_type == "forget":
        email_title = u"慕学网密码重置链接"
        email_body = u"请点击以下链接重置你的密码: http://127.0.0.1:8000/reset/{}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status:
            # TODO
            print u"发送成功！"


def random_str(random_length=16):
    """默认选取16位随机字符串"""
    code = ''
    chars = string.ascii_letters + str(string.digits)
    lengths = len(chars) - 1

    for i in range(random_length):
        code += chars[randint(0, lengths)]

    return code

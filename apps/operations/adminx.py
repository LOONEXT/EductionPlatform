# -*- coding:utf-8 -*-

import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ["name", "mobile", "course_name", "add_time"]
    search_fields = ["name", "mobile", "course_name"]
    list_filter = ["name", "mobile", "course_name", "add_time"]


class CourseCommentsAdmin(object):
    list_display = ["course", "user", "comments", "add_time"]
    search_fields = ["course", "user"]
    list_filter = ["course", "user", "add_time"]


class UserFavoriteAdmin(object):
    list_display = ["user", "fav_id", "fav_type", "add_time"]
    search_fields = ["user", "fav_type"]
    list_filter = ["user", "fav_type", "add_time"]


class UserMessageAdmin(object):
    list_display = ["user", "message", "is_read", "add_time"]
    search_fields = ["user"]
    list_filter = ["user", "is_read", "add_time"]


class UserCourseAdmin(object):
    list_display = ["user", "course", "add_time"]
    search_fields = ["user", "course"]
    list_filter = ["user", "course", "add_time"]


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)

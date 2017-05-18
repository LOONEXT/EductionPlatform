# -*- coding:utf-8 -*-

import xadmin

from .models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ["name", "add_time"]
    search_fields = ["name"]


class CourseOrgAdmin(object):
    list_display = ["name", "city", "address", "click_nums", "fav_nums", "add_time"]
    search_fields = ["name", "city", "address"]
    list_filter = ["city", "add_time"]


class TeacherAdmin(object):
    list_display = ["name", "org", "points", "work_postion", "work_years", "fav_nums"]
    search_fields = ["name", "org", "points", "work_years", "work_postion"]
    list_filter = ["work_years", "work_company", "work_postion", "points", "add_time"]


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

from util import TimeUtil
"""
整体思路：因为不知道有几门课程，几门成绩，将成绩以学号
加课程名存在school里面，取得成绩的时候通过遍历。教师教授的课程也同理
使用is_stu和is_tea区分学生和教师
"""


class Change:   # change类作为父类集成给其他子类精简代码

    def __init__(self, username, password, year, month, day, achievement, salary):
        self.username = username
        self.password = password
        self.year = year
        self.month = month
        self.day = day
        self.achievement = achievement
        self.util = TimeUtil()
        self.salary = salary
        self.xz = None
        self.sz = None

    def change_my_username(self, new_username):
        self.username = new_username

    def change_my_password(self, new_password):
        self.password = new_password

    def user_login(self, password):
        if self.password == password:
            return True
        else:
            return False

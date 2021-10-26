from user import Admin, Student, Teacher, Score
from util import TimeUtil
from menu import Menu


class School:
    def __init__(self):
        self.menu = Menu()
        self.admin_list = list()
        self.tea_list = list()

    @staticmethod
    def show_user_list(info_list):
        for info in info_list:
            info.show_info()

    def login(self, choice):
        """
        登录函数，通过choice传入选择的用户类型
        :param choice: 1为学生，2为教师，3为管理员
        :return: 登录的用户
        """
        num = 0
        while num < 3:
            

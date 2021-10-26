from user import Admin, Student, Teacher, Score
from util import TimeUtil
from menu import Menu


class ClassList:
    def __init__(self):
        self.class_list = list()

    def choice_class(self, class_id):
        num = 0
        for class_info in self.class_list:
            if class_info[0] == class_id:
                return class_info[0]
            else:
                num += 1
            if num == len(self.class_list):
                return RuntimeError

    def add_class(self, class_id, class_name):
        for class_list in self.class_list:
            if class_list[0] == class_id:
                return RuntimeError
        temp = class_id, class_name
        self.class_list.append(temp)


class School(ClassList):
    def __init__(self):
        super(ClassList).__init__()
        self.menu = Menu()
        self.admin_list = list()
        self.tea_list = list()
        self.stu_list = list()

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
            user = None
            username, password = self.menu.get_login_info()
            login = None
            if choice is 1 and isinstance(username, int):
                for user in self.stu_list:
                    if user.sno == username:
                        login = user.login(password)
            elif choice is 2 and isinstance(username, int):
                for user in self.tea_list:
                    if user.tno == username:
                        login = user.login(password)
            elif choice is 3 and isinstance(username, int):
                for user in self.admin_list:
                    if user.uid == username:
                        login = user.login(password)
            elif choice is 1:
                for user in self.stu_list:
                    if user.username == username:
                        login = user.login(password)
            elif choice is 2:
                for user in self.tea_list:
                    if user.username == username:
                        login = user.login(password)
            elif choice is 3:
                for user in self.admin_list:
                    if user.username == username:
                        login = user.login(password)
            if login:
                return user
            num += 1

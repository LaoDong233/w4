from util import TimeUtil
"""
主思路：
创建admin，teacher，stu的菜单，
然后通过不同的方式以及权限遍历出来不同的内容，
达到简洁代码的目的。
"""


class Menu:
    def __init__(self):
        self.time_util = TimeUtil()
        # 登录方式菜单
        self.login_mode_menu = {
            1: "Sno/Tno/Uid",
            2: "Username",
            3: "Back",
            4: "Exit"
        }
        # 登录菜单
        self.login_menu = {
            1: 'Student',
            2: 'Teacher',
            3: 'Administrator',
            4: 'End'
        }
        # 管理员需要选择用户时的选项
        self.admin_operate_user_menu = {
            1: "Student",
            2: "Teacher",
            3: "Administrator"
        }
        # 管理员主菜单
        self.admin_menu = {
            1: "Change Password",
            2: "Change Username",
            3: "Add User",
            4: "Remove User",
            5: "Show User",
            6: "Change Other Info",
            7: "Change Other Password",
            8: "Show Class",
            9: "Add Class",
            10: "Remove Class",
            11: "Back",
            12: "Exit"
        }
        # 教师菜单
        self.tea_menu = {
            1: "Change Password",
            2: "Change Username",
            3: "Change Info",
            4: "Add Student",
            5: "Remove Student",
            6: "Show Student",
            7: "Change Student Password",
            8: "Change Student Info",
            9: "Change Student Score",
            10: "Back",
            11: "Exit"
        }
        # 学生菜单
        self.stu_menu = {
            1: "Change Password",
            2: "Change Username",
            3: "Change Info",
            4: "Show Score",
            5: "Show Info",
            6: "Back",
            7: "Exit"
        }
        # 两个报错
        self.run_time_error_info = 'Input Error!'
        self.value_error_info = 'ValueError!'

    def get_level(self, administrator):
        """
        没什么鸟用的函数，用来获取传进来的管理员的等级，用来统一传入的数据
        :param administrator: 传入管理员
        :return: 返回管理员的级别，或者报错
        """
        if not isinstance(administrator.level, int):
            print(self.run_time_error_info)
            return RuntimeError
        else:
            return administrator.level

    def show_admin_menu(self, user):
        """
        显示管理员菜单,根据等级决定要显示的部分
        :param user: 需要传入登陆的管理员
        :return: None
        """
        level = self.get_level(user)
        for number, item in self.admin_menu.items():
            if level == 1 and number not in [1, 2, 3, 4, 5, 11, 12]:
                break
            else:
                print("%s-----%s" % (number, item))

    def show_admin_user_choice(self, user):
        """
        显示管理员选择用户的时候的菜单，如果传入的user为None则按照1处理
        :param user: 需要传入登陆的管理员
        :return: None
        """
        if user is None:
            level = 1
        else:
            level = self.get_level(user)
        for number, item in self.admin_operate_user_menu.items():
            if level == 1 and number is 3:
                continue
            else:
                print("%s-----%s" % (number, item))

    def get_info(self):
        """
        通过get info函数获取change所需要的变量
        :return:年份，月份和日期
        """
        while 1:
            try:
                year = int(input('What is your birth year: '))
                self.time_util.check_year(year)
                month = int(input('What is your birth month: '))
                self.time_util.check_month(month)
                day = int(input("What is your birth day: "))
                self.time_util.check_day(year, month, day)
            except RuntimeError:
                print(self.run_time_error_info)
                continue
            except ValueError:
                print(self.value_error_info)
                continue
            else:
                return year, month, day

    @staticmethod
    def get_login_info():
        """
        获取用户名密码函数，传入choice给程序判断是选择学号登录还是选择用户名登录
        :return: 用户名或者学号
        """
        while 1:
            usr = None
            pas = None
            try:
                usr = input("Input your username: ")
                if usr == '':
                    continue
                pas = input("Input your password: ")
                if pas == '':
                    continue
                id_usr = int(usr)
            except ValueError:
                return usr, pas
            else:
                return id_usr, pas

    def get_choice_login(self):
        """
        用来获取登录的用户类型的函数
        :return: 返回选择的数值
        """
        while 1:
            try:
                choice = int(input("Enter your choice: "))
                if choice not in [1, 2, 3]:
                    raise RuntimeError
            except RuntimeError:
                print(self.run_time_error_info)
                continue
            except ValueError:
                print(self.value_error_info)
                continue
            else:
                return choice

    def get_choice_login_mode(self):
        """
        用来获取使用什么信息登录的函数
        :return: 返回选择的数值
        """
        while 1:
            try:
                choice = int(input("Enter your choice: "))
                if choice not in range(1, 5):
                    raise RuntimeError
            except RuntimeError:
                print(self.run_time_error_info)
                continue
            except ValueError:
                print(self.value_error_info)
                continue
            else:
                return choice

    @staticmethod
    def show_list(menu_list):
        for num, item in menu_list:
            print("%s-----%s" % (num, item))
        return None

    def show_login_menu(self, choice):
        """
        用来显示登录菜单，仅此而已
        :param choice:choice选择菜单，1是主菜单，2是登录方法菜单
        :return: None
        """
        if choice is 1:
            self.show_list(self.login_mode_menu)
        else:
            self.show_list(self.login_menu)
        return None

    @staticmethod
    def separator():
        """
        一条奇怪的分割线
        :return: None
        """
        print("=" * 20)
        return None

    def show_tea_menu(self):
        self.show_list(self.tea_menu)

    def show_stu_menu(self):
        self.show_list(self.stu_menu)

    def get_new_user(self, user_type):
        """
        获取一个新的用户
        :param user_type:获取的用户类型，1为学生，2为教师，3为学生
        :return: 返回需要的用户信息
        """
        while 1:
            usr = int(input("Input user's username: "))
            pas = int(input("Input user's password: (def: 123"))
            # if判断是否为空
            if usr == '':
                continue
            if pas == '':
                pas = 123
            uid = None
            try:
                if user_type == 1:
                    uid = int(input("Input user's sno: "))
                elif user_type == 2:
                    uid = int(input("Input user's tno: "))
                elif user_type == 3:
                    return usr, pas
            except ValueError:
                print(self.value_error_info)
                continue
            else:
                return uid, usr, pas

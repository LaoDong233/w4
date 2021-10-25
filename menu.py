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
        # 登录菜单
        self.login_menu = {
            1: 'Student',
            2: 'Teacher',
            3: 'Administrator',
            4: 'End'
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

        }
        # 两个报错
        self.run_time_error_info = 'Input Error!'
        self.value_error_info = 'ValueError!'
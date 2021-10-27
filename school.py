from user import Admin, Student, Teacher
from menu import Menu


class ClassList:
    def __init__(self):
        self.class_list = list()

    def choice_class(self, class_id):
        """
        传入class id返回一个课程名
        :param class_id: 一个班级的id
        :return: 返回这个班级的名字
        """
        num = 0
        for class_info in self.class_list:
            if class_info[0] == class_id:
                return class_info[0]
            else:
                num += 1
            if num == len(self.class_list):
                return RuntimeError

    def add_class(self, class_id, class_name):
        """
        传入一个班级id和一个班级名称，查重后添加到课程目录
        :param class_id: 课程id
        :param class_name: 课程名称
        :return: 返回空
        """
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
        """
        一个静态函数，传入一个用户列表，返回里面所有用户信息
        :param info_list:
        :return:
        """
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

    @staticmethod
    def get_info_number(info_list):
        """
        传入一个列表，返回中间间隔的uid，或者返回最后一个
        :param info_list: 用户列表
        :return: 返回可以用的Uid
        """
        size = 0
        for info in info_list:
            if not info.uid == (size + 1):
                return info.uid - 1
            else:
                size = info.uid
        else:
            return size + 1

    def add_new_user(self, choice, user):
        """
        复合型添加用户，根据传入的参数进行多次判断
        :param choice:传入要添加的用户类型。1为学生，2为教师，3为管理员
        :param user:
        :return:
        """
        num = 0
        while 1:
            cant_add = None
            if num < 3:
                uid, username, password = self.menu.get_new_user(choice)
                if choice == 1:
                    for info in self.stu_list:
                        if info.sno == uid:
                            cant_add = False
                        elif info.username == username:
                            cant_add = True
                elif choice == 2:
                    for info in self.tea_list:
                        if info.tno == uid:
                            cant_add = False
                        elif info.username == username:
                            cant_add = True
                elif choice == 3:
                    for info in self.admin_list:
                        if info.username == username:
                            cant_add = True
                if isinstance(cant_add, bool):
                    if cant_add:
                        print("username error")
                        continue
                    else:
                        print("sno/tno error")
                        continue
                else:
                    # 这里的算法是先拿到UID序号中缺失的一位，然后作为新用户的UID。
                    # 最后再调用sorted进行排序
                    if choice == 3:
                        no = self.get_info_number(self.admin_list)
                        self.admin_list.append(Admin(no, username, password, uid))
                        self.admin_list = sorted(self.admin_list, key=lambda admin: admin.uid)
                    elif choice == 1:
                        no = self.get_info_number(self.stu_list)
                        self.stu_list.append(Student(no, user.uid, uid, username, password))
                        self.stu_list = sorted(self.stu_list, key=lambda student: student.uid)
                    elif choice == 2:
                        no = self.get_info_number(self.tea_list)
                        self.tea_list.append(Teacher(no, uid, username, password))
                        self.stu_list = sorted(self.tea_list, key=lambda teacher: teacher.uid)
                num += 1
            print("add user error")

    def show_list(self, info_list, user):
        """
        复合型显示用户列表
        :param info_list: 传入一个用户列表
        :param user: 当是教师时传入教师，如果传入则只显示教师管理的学生
        :return:
        """
        if user is None:
            for info in info_list:
                info.show_info()
        else:
            stu_list = self.get_tea_stu(user)
            for info in stu_list:
                info.show_info()

    def get_tea_stu(self, user):
        """
        寻找教师管理的学生
        :param user: 传入一个老师
        :return: 返回传入的教师所管理的所有学生的列表
        """
        tea_stu_list = list()
        for stu in self.stu_list:
            if stu.tid == user.uid:
                tea_stu_list.append(stu)
        return tea_stu_list

    def add_class_teacher(self, user, class_id):
        """
        为一个老师添加一个课程，先在班级里面寻找有没有这个课程，如果没有则添加失败，如果有则将课程id存入教师类列表中
        :param user: 传入一个教师
        :param class_id: 传入一个课程的id
        :return:
        """
        can_add = None
        for class_info in self.class_list:
            if class_info.class_id == class_id:
                can_add = True
        if can_add:
            user.class_list.append(class_id)
        else:
            print("add error")

    def tea_change_score(self, user, student, class_id, score):
        stu_list = self.get_tea_stu(user)
        for stu in stu_list:
            if stu.sno == student:
                self.stu_list.remove(stu)
                stu.add_score(class_id, score, user.tno)

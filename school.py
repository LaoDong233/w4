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
            if choice == 1 and isinstance(username, int):
                for user in self.stu_list:
                    if user.sno == username:
                        login = user.user_login(password)
            elif choice == 2 and isinstance(username, int):
                for user in self.tea_list:
                    if user.tno == username:
                        login = user.user_login(password)
            elif choice == 3 and isinstance(username, int):
                for user in self.admin_list:
                    if user.uid == username:
                        login = user.user_login(password)
            elif choice == 1:
                for user in self.stu_list:
                    if user.username == username:
                        login = user.user_login(password)
            elif choice == 2:
                for user in self.tea_list:
                    if user.username == username:
                        login = user.user_login(password)
            elif choice == 3:
                for user in self.admin_list:
                    if user.username == username:
                        login = user.user_login(password)
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
        while num < 3:
            cant_add = None
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
                    break
                elif choice == 1:
                    no = self.get_info_number(self.stu_list)
                    self.stu_list.append(Student(no, user.uid, uid, username, password))
                    self.stu_list = sorted(self.stu_list, key=lambda student: student.uid)
                    break
                elif choice == 2:
                    no = self.get_info_number(self.tea_list)
                    self.tea_list.append(Teacher(no, uid, username, password))
                    self.stu_list = sorted(self.tea_list, key=lambda teacher: teacher.uid)
                    break
            num += 1
        if num != 0:
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
        """
        教师修改学生成绩函数，修改添加一体，如果存在的class_id则修改，否则添加
        :param user: 传入一个教师
        :param student: 传入一个学生的学号
        :param class_id: 传入一个课程id
        :param score: 传入一个分数
        :return:
        """
        stu_list = self.get_tea_stu(user)
        for stu in stu_list:
            if stu.sno == student:
                self.stu_list.remove(stu)
                stu.add_score(class_id, score, user.tno)

    def show_class(self, user):
        """
        在传入教师的情况下，显示教师所管理的所有课程和id，否则显示全部的课程和id
        :param user: 传入一个老师的用户
        :return:
        """
        if user is None:
            for class_info in self.class_list:
                class_id = class_info[0]
                class_name = class_info[1]
                print("Class id:%s, Class name:%s" % (class_id, class_name))
        else:
            for class_info in self.class_list:
                class_id = class_info[0]
                if class_id not in user.class_list:
                    continue
                class_name = class_info[1]
                print("Class id:%s, Class name:%s" % (class_id, class_name))

    def remove_user(self, types, user):
        """
        删除用户函数，通过types获取要删除哪一类用户，然后在选择删除教师的时候
        :param types:传入要删除的用户类型，1为学生，2为教师，3为管理员
        :param user:删除学生时传入一个教师或者一个管理员，判断显示类型
        :return:
        """
        info_list = None
        if types == 1:
            info_list = "self.stu_list"
        elif types == 2:
            info_list = "self.tea_list"
        elif types == 3:
            info_list = "self.admin_list"
        is_admin = False
        if user.level:
            is_admin = True
        if types == 2 and not is_admin:
            self.show_list(eval(info_list), user)
        else:
            self.show_list(eval(info_list), None)
        choice = self.menu.get_min_choice(len(eval(info_list))) - 1
        print(choice)
        choice_user = eval(info_list)[choice]
        if types == 2:
            for stu in self.stu_list:
                if choice_user.uid == stu.tid:
                    self.stu_list.remove(stu)
        else:
            eval(info_list).remove(choice_user)
        """
        ！！！如果删除教师则会连带删除教师管理的学生！！！
        """

    def show_user(self, user):
        choice_list = None
        if user.level:
            if user.level == 1:
                self.menu.show_admin_user_choice(user)
                choice = self.menu.get_min_choice(2)
            else:
                self.menu.show_admin_user_choice(user)
                choice = self.menu.get_min_choice(3)
            if choice == 1:
                choice_list = "self.stu_list"
            elif choice == 2:
                choice_list = "self.tea_list"
            elif choice == 3:
                choice_list = "self.admin_list"
        else:
            stu_list = self.get_tea_stu(user)
            choice_list = "stu_list"
        self.show_list(eval(choice_list), None)


if __name__ == '__main__':
    school = School()
    # 内置管理员 admin 密码 admin
    school.admin_list.append(Admin(1, 'admin', 'admin', 2))
    # 内置内置学生 a 密码 1
    school.stu_list.append(Student(1, 1, 1, "a", "1"))
    # 内置内置教师 a 密码 1
    school.tea_list.append(Teacher(1, 1, "a", "1"))
    # 内置管理员 aa 密码 aa
    school.admin_list.append(Admin(1, 'aa', 'aa', 1))
    users = school.login(2)
    school.show_user(users)
    """
    删除功能测试
    school.stu_list.append(Student(1, 1, 1, "1", "1"))
    school.tea_list.append(Teacher(1, 1, "1", 1))
    school.admin_list.append(Admin(1, 'aa', 'aa', 2))
    users = school.login(3)
    school.remove_user(2, users)
    school.show_list(school.stu_list, None)
    school.show_list(school.admin_list, None)
    """
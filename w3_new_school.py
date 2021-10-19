from w3_new_menu import Menu
from w3_user import Admin
from w3_user import Student
from w3_user import Teacher
from w3_util import TimeUtil


class School:
    def __init__(self):
        self.menu = Menu()
        self.admin_list = list()
        self.tea_list = list()
        self.stu_list = list()
        self.util = TimeUtil()

    @staticmethod
    def show_list(info_list):
        for a in info_list:
            a.show_info()

    def login(self, choice):
        """

        :param choice:传入选择的用户类型，1为学生，2为老师，3为管理员
        :return: 返回登陆成功的用户或者None
        """
        tally = 0
        pas = 0
        a = None
        num = 0
        while tally < 3:
            usr, pas = self.menu.get_login_usr()
            tally += 1
            if choice == 1:
                for a in self.stu_list:
                    if usr == a.username:
                        num = 0
                        break
                    else:
                        num += 1
                if num != 0:
                    print("Username not found: %s" % usr)
                    num = 0
                    continue
            elif choice == 2:
                for a in self.tea_list:
                    if usr == a.username:
                        num = 0
                        break
                    else:
                        num += 1
                if num != 0:
                    print("Username not found: %s" % usr)
                    num = 0
                    continue
            elif choice == 3:
                for a in self.admin_list:
                    if usr == a.username:
                        num = 0
                        break
                    else:
                        num += 1
                if num != 0:
                    print("Username not found: %s" % usr)
                    num = 0
                    continue
            break
        if tally == 3:
            return None
        if a.user_login(pas):
            print("Successful Login!")
            return a
        else:
            print("Login Filed!")
            return None

    def find_student(self, user):
        """

        :param user:传入老师的用户
        :return: 返回该老师管理的学生的列表
        """
        b = list()
        for a in self.stu_list:
            if a.pid == user.uid:
                b.append(a)
        return b

    def show_other_info(self, choice, user):
        if choice == 2:
            self.tea_show_other_info(user.uid)
        if choice == 3:
            a = None
            while 1:
                try:
                    a = int(input("1.Student\n2.Teacher\nChoice: "))
                    if not 0 < a < 3:
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                else:
                    break
            if a == 1:
                self.show_list(self.stu_list)
            elif a == 2:
                self.show_list(self.tea_list)

    def tea_show_other_info(self, pid):
        """

        :param pid:传入教师uid显示对应pid的学生
        :return: 无
        """
        for a in self.stu_list:
            if a.pid == pid:
                # print("uid:%s" % a.uid, end=" ")
                a.show_info()

    def get_new_user(self, choice, user):
        """
        :param choice:1为超级管理员，2为老师，3为普通管理员
        :param user:传入老师，寻找老师管理的学生
        :return:None
        """
        c = 0
        if choice == 2:
            b = 0
            print(c, b)
            for a in self.stu_list:
                c = a.uid
                print(c, b)
                if b == 0:
                    b = c
                    continue
                if (b + 1) != c:
                    c = b + 1
                    break
                b = c
            else:
                c += 1
            usr, pas = self.menu.get_user(choice)
            self.stu_list.insert(c - 1, Student(user.uid, c, usr, pas))
        if choice == 3:
            b = 0
            print(c, b)
            for a in self.tea_list:
                c = a.uid
                print(c, b)
                if b == 0:
                    b = c
                    continue
                if (b + 1) != c:
                    c = b + 1
                    break
                b = c
            else:
                c += 1
            usr, pas = self.menu.get_user(choice)
            self.tea_list.insert(c - 1, Teacher(c, usr, pas))
        if choice == 1:
            b = 0
            print(c, b)
            for a in self.admin_list:
                c = a.uid
                print(c, b)
                if b == 0:
                    b = c
                    continue
                if (b + 1) != c:
                    c = b + 1
                    break
                b = c
            else:
                c += 1
            usr, pas, level = self.menu.get_user(choice)
            self.admin_list.insert(c - 1, Admin(c, usr, pas, level))

    def remove_user(self, choice, user):
        """

        :param choice:1为删除管理员，2为删除学生，3为删除老师
        :param user: 如果选择2需要传入一个老师来寻找学生
        :return: 无
        """
        if choice == 2:
            num = 0
            self.tea_show_other_info(user.uid)
            s_l = self.find_student(user)
            while num < 3:
                num += 1
                try:
                    a = int(input("Please select your student which do you want remove: \nNo. "))
                    if not 0 < a <= len(s_l):
                        raise RuntimeError
                    elif s_l[a-1].pid != user.uid:
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                self.stu_list.remove(s_l[a-1])
                break
        if choice == 3:
            num = 0
            for a in self.tea_list:
                a.show_info()
            while num < 3:
                num += 1
                try:
                    a = int(input("Please select which teacher do you want remove: "))
                    if not 0 < a <= len(self.tea_list):
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                e = self.tea_list[a-1].uid
                f = list()
                # e用来存储即将删除的用户id
                self.tea_list.pop(a - 1)
                for d in self.stu_list:
                    if d.pid == e:
                        f.append(d)
                while len(f) > 0:
                    d = f.pop()
                    self.stu_list.remove(d)
                break
        if choice == 1:
            num = 0
            for a in self.admin_list:
                a.show_info()
            while num < 3:
                num += 1
                try:
                    a = int(input("Please select which admin do you want move: "))
                    if not 0 < a <= len(self.admin_list):
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                self.admin_list.pop(a - 1)
                break

    def change_other_info(self, choice, user):
        """

        :param choice: 3为管理员，2为老师，传入即可修改数据
        :param user: 传入老师修改对应的学生数据，只有选择2时需要传入
        :return:
        """
        self.menu.separator()
        num = 0
        if choice == 3:
            while num < 3:
                num += 1
                try:
                    a = int(input('Student----1\nTeacher----2\nChoice: '))
                    if a not in [1, 2]:
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                if a == 1:
                    for a in self.stu_list:
                        a.show_info()
                    while 1:
                        try:
                            b = int(input('Choice No. '))
                            if not 0 < b <= len(self.stu_list):
                                raise RuntimeError
                        except RuntimeError:
                            print(self.menu.run_time_error_info)
                            continue
                        except ValueError:
                            print(self.menu.value_error_info)
                            continue
                        c = self.stu_list[b - 1]
                        year, month, day, tally = self.menu.get_info(1)
                        c.change_info(year, month, day, tally)
                        break
                elif a == 2:
                    for a in self.tea_list:
                        a.show_info()
                    while 1:
                        try:
                            b = int(input('Choice No. '))
                            if not 0 < b <= len(self.tea_list):
                                raise RuntimeError
                        except RuntimeError:
                            print(self.menu.run_time_error_info)
                            continue
                        except ValueError:
                            print(self.menu.value_error_info)
                            continue
                        c = self.tea_list[b - 1]
                        year, month, day, tally = self.menu.get_info(1)
                        c.change_info(year, month, day, tally)
                        break
                break
        elif choice == 2:
            self.tea_show_other_info(user.uid)
            stu_list = self.find_student(user)
            while 1:
                try:
                    a = int(input('Choice No. '))
                    if not 0 < a <= len(stu_list):
                        raise RuntimeError
                    self.stu_list.remove(stu_list[a-1])
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                except ValueError:
                    print(self.menu.value_error_info)
                else:
                    break
            year, month, day, tally = self.menu.get_info(1)
            stu_list[a-1].change_info(year, month, day, tally)
            self.stu_list.append(stu_list[a-1])
            self.stu_list = sorted(self.stu_list, key=lambda student: student.uid)

    def change_other_tally(self, choice, user):
        """

        :param choice: 3为管理员，2为老师，传入即可修改数据
        :param user: 传入老师修改对应的学生数据，只有选择2时需要传入
        :return:
        """
        self.menu.separator()
        num = 0
        if choice == 3:
            while num < 3:
                num += 1
                try:
                    a = int(input('Student----1\nTeacher----2\nChoice: '))
                    if a not in [1, 2]:
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                if a == 1:
                    for a in self.stu_list:
                        a.show_info()
                    while 1:
                        try:
                            b = int(input('Choice No. '))
                            if not 0 < b <= len(self.stu_list):
                                raise RuntimeError
                        except RuntimeError:
                            print(self.menu.run_time_error_info)
                            continue
                        except ValueError:
                            print(self.menu.value_error_info)
                            continue
                        c = self.stu_list[b - 1]
                        a = 0
                        while 1:
                            try:
                                a = int(input("Please input a new achievement: "))
                            except RuntimeError:
                                print(self.menu.run_time_error_info)
                                continue
                            except ValueError:
                                print(self.menu.value_error_info)
                                continue
                            else:
                                break
                        c.change_tally(a)
                        break
                elif a == 2:
                    for a in self.tea_list:
                        a.show_info()
                    while 1:
                        try:
                            b = int(input('Choice No. '))
                            if not 0 < b <= len(self.tea_list):
                                raise RuntimeError
                        except RuntimeError:
                            print(self.menu.run_time_error_info)
                            continue
                        except ValueError:
                            print(self.menu.value_error_info)
                            continue
                        c = self.tea_list[b - 1]
                        a = 0
                        while 1:
                            try:
                                a = int(input("Please input a new salary: "))
                            except RuntimeError:
                                print(self.menu.run_time_error_info)
                                continue
                            except ValueError:
                                print(self.menu.value_error_info)
                                continue
                            else:
                                break
                        c.change_tally(a)
                        break
                break
        elif choice == 2:
            self.tea_show_other_info(user.uid)
            stu_list = self.find_student(user)
            while 1:
                try:
                    a = int(input('Choice No. '))
                    if not 0 < a <= len(stu_list):
                        raise RuntimeError
                    self.stu_list.remove(stu_list[a - 1])
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                except ValueError:
                    print(self.menu.value_error_info)
                else:
                    break
            tally = 1
            stu_list[a - 1].change_tally(tally)
            self.stu_list.append(stu_list[a - 1])
            self.stu_list = sorted(self.stu_list, key=lambda student: student.uid)
            """
            b = 0
            num = 0
            for c in self.stu_list:
                if c.uid == (stu_list[a-1].uid + 1):
                    break
                else:
                    num += 1
            self.stu_list.insert(num, stu_list[a-1])
            """

    def change_other_passwords(self, choice, user):
        """

        :param choice:1为超级管理员，2为教师，3为普通管理员
        :param user: 只有选择2的时候需要传入，锁定权限
        :return: 无
        """
        pwd = str()
        if choice == 1:
            a = 0
            while 1:
                try:
                    a = int(input('1.Teacher\n2.Student\n3.Admin\nChoice: '))
                    if a not in [1, 2, 3]:
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                else:
                    break
            self.menu.separator()
            if a == 1:
                for a in self.tea_list:
                    a.show_info()
                self.menu.separator()
                while 1:
                    try:
                        a = int(input('Choice No. '))
                        if 0 < a <= len(self.tea_list):
                            raise RuntimeError
                        pwd = input("Input a new Password: ")
                    except RuntimeError:
                        print(self.menu.run_time_error_info)
                        continue
                    except ValueError:
                        print(self.menu.value_error_info)
                        continue
                    else:
                        break
                self.tea_list[a-1].change_my_password(pwd)
                return None
            elif a == 2:
                for a in self.stu_list:
                    a.show_info()
                self.menu.separator()
                while 1:
                    try:
                        a = int(input('Choice No. '))
                        if 0 < a <= len(self.stu_list):
                            raise RuntimeError
                        pwd = input("Input a new Password: ")
                    except RuntimeError:
                        print(self.menu.run_time_error_info)
                        continue
                    except ValueError:
                        print(self.menu.value_error_info)
                        continue
                    else:
                        break
                self.stu_list[a-1].change_my_password(pwd)
            elif a == 3:
                for a in self.admin_list:
                    a.show_info()
                self.menu.separator()
                while 1:
                    try:
                        a = int(input('Choice No. '))
                        if 0 < a <= len(self.admin_list):
                            raise RuntimeError
                        pwd = input("Input a new Password: ")
                    except RuntimeError:
                        print(self.menu.run_time_error_info)
                        continue
                    except ValueError:
                        print(self.menu.value_error_info)
                        continue
                    else:
                        break
                self.admin_list[a-1].change_my_password(pwd)
        elif choice == 2:
            a = 0
            stu_list = self.find_student(user)
            self.menu.separator()
            self.show_list(stu_list)
            while 1:
                try:
                    a = int(input('Choice No. '))
                    if not 0 < a <= len(stu_list):
                        raise RuntimeError
                except RuntimeError:
                    print(self.menu.run_time_error_info)
                    continue
                except ValueError:
                    print(self.menu.value_error_info)
                    continue
                else:
                    break
            self.stu_list.remove(stu_list[a-1])
            pwd = self.menu.get_password()
            stu_list[a-1].change_my_password(pwd)
            self.stu_list.append(stu_list[a-1])
            self.stu_list = sorted(self.stu_list, key=lambda student: student.uid)

    def get_username(self, choice):
        while 1:
            try:
                user = input("Input a New Username: ")
                if choice == 1:
                    for a in self.stu_list:
                        if a.username == user:
                            raise RuntimeError
                elif choice == 2:
                    for a in self.tea_list:
                        if a.username == user:
                            raise RuntimeError
                elif choice == 3:
                    for a in self.admin_list:
                        if a.username == user:
                            raise RuntimeError
            except RuntimeError:
                print(self.menu.run_time_error_info)
                continue
            except ValueError:
                print(self.menu.value_error_info)
                continue
            else:
                return user

    def start(self):
        self.admin_list.append(Admin(1, "root", "123", 2))
        while 1:
            user = None
            end = False
            num = 0
            self.menu.show_choice()
            first_choice = self.menu.get_choice(True)
            while num < 3:
                try:
                    user = self.login(first_choice)
                    num += 1
                    if user is None:
                        raise AttributeError
                except AttributeError:
                    print("No users in zhe list!")
                    end = True
                    break
                else:
                    end = False
                    break
            if num == 3:
                continue
            if end:
                continue
            while 1:
                if first_choice == 3 and user.level == 1:
                    self.menu.show_menu(4)
                    sen_choice = self.menu.get_choice(4)
                else:
                    self.menu.show_menu(first_choice)
                    sen_choice = self.menu.get_choice(first_choice)
                if sen_choice == 1:
                    user.change_my_password(self.menu.get_password())
                elif sen_choice == 2:
                    user.change_my_username(self.get_username(first_choice))
                elif sen_choice == 3:
                    year, month, day, tally = self.menu.get_info(first_choice)
                    user.change_info(year, month, day, tally)
                elif sen_choice == 4:
                    user.show_info()
                elif sen_choice == 5:
                    a = self.menu.get_tally(first_choice)
                    user.change_tally(a)
                elif sen_choice == 6:
                    self.change_other_info(first_choice, user)
                elif sen_choice == 7:
                    if first_choice == 3 and user.level == 2:
                        choice = 0
                        while 1:
                            try:
                                choice = int(input("1.Teacher\n2.Admin\nChoice:"))
                                if not 0 < choice < 3:
                                    raise RuntimeError
                            except ValueError:
                                print(self.menu.run_time_error_info)
                                continue
                            except RuntimeError:
                                print(self.menu.run_time_error_info)
                                continue
                            else:
                                break
                        if choice == 2:
                            self.get_new_user(1, None)
                        else:
                            self.get_new_user(first_choice, user)
                    else:
                        self.get_new_user(first_choice, user)
                elif sen_choice == 8:
                    if first_choice == 3 and user.level == 2:
                        thr_choice = None
                        while 1:
                            try:
                                thr_choice = int(input("1.Admin\n2.Teacher\nChoice: "))
                                if not 0 < thr_choice < 3:
                                    raise RuntimeError
                                if thr_choice == 2:
                                    thr_choice = 3
                            except RuntimeError:
                                print(self.menu.run_time_error_info)
                                continue
                            except ValueError:
                                print(self.menu.value_error_info)
                                continue
                            else:
                                break
                        self.remove_user(thr_choice, None)
                    else:
                        self.remove_user(first_choice, user)
                elif sen_choice == 9:
                    self.show_other_info(first_choice, user)
                elif sen_choice == 10:
                    self.change_other_tally(first_choice, user)
                elif sen_choice == 11:
                    if first_choice == 3 and user.level == 2:
                        self.change_other_passwords(1, None)
                    else:
                        self.change_other_passwords(first_choice, user)
                elif sen_choice == 12:
                    break
                elif sen_choice == 13:
                    end = True
                    break
            if end:
                break


if __name__ == '__main__':
    aa = School()
    aa.stu_list.append(Student(1, 1, 'aaa', 'aaa'))
    aa.tea_list.append(Teacher(1, '123', '123'))
    aa.stu_list.append(Student(1, 3, 'bbb', 'aaa'))
    aa.stu_list.append(Student(1, 4, 'ccc', 'aaa'))
    aa.admin_list.append(Admin(1, 'admin', str('admin'), 1))
    aa.admin_list.append(Admin(1, 'admin2', str('admin'), 1))
    bb = aa.tea_list[0]
    # aa.remove_user(2, bb)
    aa.change_other_tally(2, bb)
    aa.tea_show_other_info(1)
    for aaaa in aa.stu_list:
        print("uid:%s " % aaaa.uid, end="")
        aaaa.show_info()
    for aaaa in aa.admin_list:
        aaaa.show_info()
    for aaaa in aa.tea_list:
        aaaa.show_info()
    # aa.login(3)

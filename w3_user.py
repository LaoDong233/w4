from util import TimeUtil


class Change:

    def __init__(self, username, passwd, year, month, day, achievement, salary):
        self.username = username
        self.passwd = passwd
        self.year = year
        self.month = month
        self.day = day
        self.util = TimeUtil()
        self.achievement = achievement
        self.salary = salary
        self.xz = None
        self.sx = None

    def change_my_username(self, new_username):
        self.username = new_username

    def change_my_password(self, new_password):
        self.passwd = new_password

    def user_login(self, password):
        if self.passwd == password:
            return True
        else:
            return False

    def change_info(self, year, month, day, tally):
        if isinstance(self.salary, bool) and isinstance(self.achievement, bool):
            return None
        self.year = year
        self.month = month
        self.day = day
        if isinstance(self.salary, bool):
            self.achievement = tally
        else:
            self.salary = tally
        self.xz = self.util.check_xz(month, day)
        self.sx = self.util.check_sx(year)

    def change_tally(self, new_tally):
        if isinstance(self.salary, bool):
            if isinstance(self.achievement, bool):
                return None
            self.achievement = new_tally
        else:
            self.salary = new_tally

    def show_info(self):
        if isinstance(self.salary, bool):
            if isinstance(self.achievement, bool):
                print("管理员%s" % self.username)
            else:
                print("%s同学%s年%s月%s日出生,属%s,星座为%s.成绩为%s" % (self.username, self.year, self.month, self.day,
                                                           self.sx, self.xz, self.achievement))
        else:
            print("%s,您于%s年%s月%s日出生,薪资%s,属%s,星座为%s" % (self.username, self.year, self.month, self.day,
                                                       self.salary, self.sx, self.xz))


class Admin(Change):
    def __init__(self, uid, username, passwd, level):
        self.uid = uid
        self.username = username
        self.passwd = passwd
        self.level = level
        self.year = None
        self.day = None
        self.month = None
        self.xz = None
        self.sx = None
        self.achievement = False
        self.salary = False
        Change.__init__(self, username, passwd, self.year, self.month, self.day, self.achievement, self.salary)

        """
        1级只可以更改教师
        2级有全部权限
        """


class Student(Change):
    def __init__(self, pid, uid, username, passwd):
        self.salary = True
        self.pid = pid
        self.uid = uid
        self.passwd = passwd
        self.username = username
        self.year = None
        self.day = None
        self.month = None
        self.xz = None
        self.sx = None
        self.achievement = None
        Change.__init__(self, username, passwd, self.year, self.month, self.day, self.achievement, self.salary)


class Teacher(Change):
    def __init__(self, uid, username, passwd):
        self.salary = None
        self.uid = uid
        self.passwd = passwd
        self.username = username
        self.year = None
        self.day = None
        self.month = None
        self.xz = None
        self.sx = None
        self.achievement = False
        Change.__init__(self, username, passwd, self.year, self.month, self.day, self.achievement, self.salary)


if __name__ == '__main__':
    a = Admin(1, 'aa', 'aa', 2)
    b = Student(1, 1, "1", "1")
    c = Teacher(1, "1", 1)
    a.change_info(1, 1, 1, 1)
    b.change_info(1, 1, 1, 1)
    c.change_info(1, 1, 1, 1)
    a.show_info()
    b.show_info()
    c.show_info()

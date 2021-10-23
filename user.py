from util import TimeUtil

"""
整体思路：因为不知道有几门课程，几门成绩，直接存在student
的一个列表里，通过遍历取出
使用is_stu和is_tea区分学生和教师
"""


class Change:  # change类作为父类集成给其他子类精简代码

    def __init__(self, username, password, year, month, day, is_stu, is_tea, level):  # 导入所有需要的数据
        self.username = username
        self.password = password
        self.year = year
        self.month = month
        self.day = day
        self.is_stu = is_stu
        self.is_tea = is_tea
        self.level = level
        self.util = TimeUtil()
        self.xz = None
        self.sx = None

    def change_my_username(self, new_username):  # 修改本用户的用户名
        self.username = new_username

    def change_my_password(self, new_password):  # 修改本用户的密码
        self.password = new_password

    def user_login(self, password):  # 登录检查
        if self.password == password:
            return True
        else:
            return False

    def change_my_info(self, year, month, day):  # 修改本用户信息
        if not self.is_stu:
            if not self.is_tea:  # 根据is_tea和is_stu判断职位，如果全否则为管理员
                return None
        self.year = year
        self.month = month
        self.day = day
        self.xz = self.util.check_xz(month, day)
        self.sx = self.util.check_sx(year)

    def show_info(self):  # 显示用户信息
        if not self.is_stu:
            if not self.is_tea:  # 判断规则同上
                print("管理员:%s，%s级" % (self.username, self.level))
            else:
                print("%s,您于%s年%s月%s日出生,属%s,星座为%s" % (self.username, self.year, self.month, self.day,
                                                      self.sx, self.xz))
        else:
            print("%s同学%s年%s月%s日出生,属%s,星座为%s" % (self.username, self.year, self.month, self.day,
                                                 self.sx, self.xz))


"""
全部将用户属性声明为None，不在一开始录入的时候录入。
录入完一个用户以后可以选择调用那个用户
的change_my_info修改或者让用户自行修改
"""


class Admin(Change):
    def __init__(self, uid, username, password, level):  # uid为系统分配，用于排序等等选取等等
        super().__init__(username, password, None, None, None, False, False, level)
        self.uid = uid

        """
        1级只可以更改教师
        2级拥有全部权限
        """


class Student(Change):
    def __init__(self, uid, tid, sno, username, password):  # tid为该学生管理的老师的uid，sno为学号
        super().__init__(username, password, None, None, None, True, False, None)
        self.uid = uid
        self.tid = tid
        self.sno = sno
        self.score = list()

    def change_score(self, class_id, new_score):
        num = 0
        for score in self.score:
            if score.class_id == class_id:
                self.score[num].score = new_score
            else:
                num += 1
            if num == len(self.score):
                return RuntimeError

    def add_score(self, score):
        self.score.append(score)


class Teacher(Change):
    def __init__(self, uid, tno, username, password):       # tno为教师工号
        super().__init__(username, password, None, None, None, False, True, False)
        self.uid = uid
        self.tno = tno


class Score:
    def __init__(self, class_id, class_name, score):
        self.class_id = class_id
        self.class_name = class_name
        self.score = score


if __name__ == '__main__':
    a = Admin(1, 'aa', 'aa', 2)
    b = Student(1, 1, 1, "1", "1")
    c = Teacher(1, 1, "1", 1)
    a.change_my_info(1, 1, 1)
    b.change_my_info(1, 1, 1)
    c.change_my_info(1, 1, 1)
    a.show_info()
    b.show_info()
    c.show_info()

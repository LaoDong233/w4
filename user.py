from util import TimeUtil

"""
整体思路：因为不知道有几门课程，几门成绩，直接存在student
的一个列表里，通过遍历取出
使用is_stu和is_tea区分学生和教师
教师拥有class列表，用于标识是否有权限添加成绩
"""


class Change:  # change类作为父类集成给其他子类精简代码

    def __init__(self, uid, username, password, year, month, day, is_stu, is_tea, level):  # 导入所有需要的数据
        self.uid = uid
        self.username = username
        self.password = password
        self.year = year
        self.month = month
        self.day = day
        self.name = None
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

    def change_my_info(self, name, year, month, day):  # 修改本用户信息
        if not self.is_stu:
            if not self.is_tea:  # 根据is_tea和is_stu判断职位，如果全否则为管理员
                return None
        self.year = year
        self.name = name
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
        """
        管理员类中uid使用系统自动分配，方便管理和排序
        :param uid: 系统分配
        :param username: 用户名
        :param password: 密码
        :param level: 管理员级别
        """
        super().__init__(uid, username, password, None, None, None, False, False, level)

        """
        1级只可以更改教师
        2级拥有全部权限
        """


class Student(Change):
    def __init__(self, uid, tid, sno, username, password):  # tid为该学生管理的老师的uid，sno为学号
        """
        uid，tid，分别为系统分配的id和管理学生的教师的id，sno为学号
        :param uid: 系统分配
        :param tid: 管理这个学生的教师uid
        :param sno: 学号
        :param username: 用户名
        :param password: 密码
        """
        super().__init__(uid, username, password, None, None, None, True, False, None)
        self.tid = tid
        self.sno = sno
        self.score = list()

    def change_score(self, class_id, new_score, tno):
        """
        关于修改分数,传入class id，和tno，找到该学生相同的class id并删除这个分数，重新打包并添加到self.score后面,
        如果没有相同的则直接添加
        :param class_id: 班级id
        :param new_score: 新分数
        :param tno: 传入修改者的uid，用来查询修改者
        :return: 如果找不到这个学科则报错
        """
        num = 0
        for score in self.score:
            if score.class_id == class_id:
                num = 0
                self.score.remove(score)
                temp = Score(class_id, new_score, tno)
                self.score.append(temp)
            else:
                num += 1
            if num == len(self.score):
                temp = Score(class_id, new_score, tno)
                self.score.append(temp)


class Teacher(Change):
    def __init__(self, uid, tno, username, password):       # tno为教师工号
        """
        和学生类似。就是减少了sno，添加了tno（教职工号）
        :param uid: 系统分配id
        :param tno: 工号
        :param username: 用户名
        :param password: 密码
        """
        super().__init__(uid, username, password, None, None, None, False, True, False)
        self.tno = tno
        self.class_list = list()


class Score:
    def __init__(self, class_id, score, tno):
        """
        分数储存类，用于封装分数，没什么大用
        :param class_id: 班级id
        :param score: 分数
        :param tno: 修改者的id
        """
        self.class_id = class_id
        self.score = score
        self.tno = tno


"""
回头移动到School里面
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
"""


if __name__ == '__main__':
    a = Admin(1, 'aa', 'aa', 2)
    b = Student(1, 1, 1, "1", "1")
    c = Teacher(1, 1, "1", 1)
    a.change_my_info(1, 1, 1, 1)
    b.change_my_info(1, 1, 1, 1)
    c.change_my_info(1, 1, 1, 1)
    a.show_info()
    b.show_info()
    c.show_info()

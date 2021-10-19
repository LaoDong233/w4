class TimeUtil:
    def __init__(self):
        self.mon_30 = [4, 6, 9, 11]
        self.mon_31 = [1, 3, 5, 7, 8, 10, 12]
        self.sx_data = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
        self.xz_name = ['水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']
        self.xz_data = 21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22

    def check_sx(self, year):
        return self.sx_data[year % 12 - 4]

    def check_xz(self, month, day):
        # 判断对应的月份中，此日期是否比分界日期大
        if self.xz_data[month - 1] <= day:
            # 返回对应星座
            return self.xz_name[month - 1]
        # 否则

        else:
            # 返回对应星座前一个星座
            return self.xz_name[month - 2]

    def check_day(self, year, month, day):
        if day <= 0:
            raise RuntimeError
        elif month in self.mon_30:
            if day > 30:
                raise RuntimeError
        elif month in self.mon_31:
            if day > 31:
                raise RuntimeError
        elif month == 2:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                if day > 29:
                    raise RuntimeError
            else:
                if day > 28:
                    raise RuntimeError
        else:
            raise RuntimeError

    @staticmethod
    def check_month(month):
        if not 0 < month <= 12:
            raise RuntimeError

    @staticmethod
    def check_year(year):
        if not year > 0:
            raise RuntimeError

    @staticmethod
    def check_achievement(achievement):
        if not achievement >= 0:
            raise RuntimeError

    @staticmethod
    def check_salary(salary):
        if not salary >= 0:
            raise RuntimeError

from util import TimeUtil


class Menu:
    def __init__(self):
        self.time_util = TimeUtil()
        self.choice_menu = {
            1: 'Student',
            2: 'Teacher',
            3: 'Administrator'
        }
        self.main_menu = {
            # √
            1: "Change Password",
            # √
            2: "Change Username",
            # √
            3: "Change Info",
            # √
            4: "Show Info",
            # √
            5: "Change Tally",
            # √
            6: "Change Other Info",
            # √
            7: "Add User",
            # √
            8: "Remove User",
            # √
            9: "Show Other Info",
            # √
            10: "Change Other Tally",
            # √
            11: "Change Other Password",
            # √
            12: "Back",
            # √
            13: "Exit"
        }
        self.run_time_error_info = 'InputError! Input Again!'
        self.value_error_info = 'ValueError! Input Again!'

    @staticmethod
    def separator():
        print('=' * 20)

    def get_password(self):
        while 1:
            try:
                pwd = input("Please enter a new password")
                return pwd
            except ValueError:
                print(self.value_error_info)
                continue

    def get_user(self, choice):
        while 1:
            usr = input("Please input your username: ")
            if usr == '':
                continue
            pas = input("Please input your password: ")
            if pas == '':
                continue
            if choice == 1:
                while 1:
                    try:
                        level = int(input("Please input your level: "))
                        if level in [1, 2]:
                            return usr, pas, level
                        else:
                            raise RuntimeError
                    except RuntimeError:
                        print(self.run_time_error_info)
                    except ValueError:
                        print(self.value_error_info)
            return usr, pas

    def show_choice(self):
        self.separator()
        for x, y in self.choice_menu.items():
            print("%s--%s" % (x, y))
        self.separator()

    def show_menu(self, choice):
        self.separator()
        for x, y in self.main_menu.items():
            if choice == 1:
                if x in [5, 6, 7, 8, 9, 10, 11]:
                    continue
            if choice == 2:
                if x in [10]:
                    continue
            if choice == 3:
                if x in [3, 5]:
                    continue
            if choice == 4:
                if x not in [7, 8, 12, 13]:
                    continue
            print("%s--%s" % (x, y))
        self.separator()

    def get_login_usr(self):
        while 1:
            username = None
            password = None
            try:
                username = input("Give me your name: ")
                password = input("Give me your password: ")
            except ValueError:
                print(self.value_error_info)
                continue
            else:
                break
        return username, password

    def get_tally(self, choice):
        while 1:
            try:
                a = None
                if choice == 1:
                    a = int(input("Input a new achievement: "))
                if choice == 2:
                    a = int(input("Input a new salary: "))
            except RuntimeError:
                print(self.run_time_error_info)
                continue
            except ValueError:
                print(self.value_error_info)
                continue
            else:
                return a

    def get_info(self, choice):
        while 1:
            try:
                tally = 0
                year = int(input('What is your birth year: '))
                self.time_util.check_year(year)
                month = int(input('What is your birth month: '))
                self.time_util.check_month(month)
                day = int(input("What is your birth day: "))
                self.time_util.check_day(year, month, day)
                if choice == 1:
                    tally = int(input("What is your achievement: "))
                elif choice == 2:
                    tally = int(input("What is your salary: "))
                return year, month, day, tally
            except RuntimeError:
                print(self.run_time_error_info)
                continue
            except ValueError:
                print(self.value_error_info)
                continue

    def get_choice(self, choice):
        a = 0
        while 1:
            try:
                a = int(input('Choice: '))
                if isinstance(choice, bool):
                    if not 0 < a < 4:
                        raise RuntimeError
                elif choice == 1:
                    if not 0 < a <= 13 and a not in [5, 6, 7, 8, 9, 10, 11]:
                        raise RuntimeError
                elif choice == 2:
                    if not 0 < a <= 13 and a != 10:
                        raise RuntimeError
                elif choice == 3:
                    if not 0 < a <= 13 and a not in [3, 5]:
                        raise RuntimeError
                elif choice == 4:
                    if not 6 < a <= 13 and a not in [9, 10, 11]:
                        raise RuntimeError
            except RuntimeError:
                print(self.run_time_error_info)
                continue
            except ValueError:
                print(self.value_error_info)
                continue
            else:
                break
        return a


if __name__ == '__main__':
    menu = Menu()
    menu.show_choice()
    aa = menu.get_choice(True)
    menu.show_menu(aa)
    bb = menu.get_choice(aa)

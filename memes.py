import datetime
from datetime import date

class Memer_and_lover:
    def __init__(self, f_name, l_name, DOB, kind_one, kind_two, kind_three, single, attracted_to, religion, year, month, day, age = 0):
        self.f_name = f_name
        self.l_name = l_name
        self.kind_one = kind_one
        self.kind_two = kind_two
        self.kind_three = kind_three
        self.single = single
        self.attracted_to = attracted_to
        self.religion = religion
        self.year = year
        self.month = month
        self.day = day
        self.age = date.today().year - self.year
        self.DOB = datetime.datetime(self.year, self.month, self.day)



    @property
    def change_sex(self):
        return self.sex
    @change_sex.setter
    def change_sex(self, new_gender):
        self.sex = new_gender
    @property
    def rt_DOB(self):
        return self.DOB
    @rt_DOB.setter
    def rt_DOB(self):
        self.DOB = datetime.datetime(self.year, self.month, self.day)
    @property
    def create_age(self):
        return self.age
    @create_age.setter
    def create_age(self):
        self.age = date.today().year - self.year



x = Memer_and_lover("xiaong", "wong", 4, "dark", "sports", "education", True, {"males", "females", "ramen"}, "muslim",2003, 7, 3, 0)


print(x.rt_DOB)
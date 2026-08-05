# Property decorator
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property
    def calcPercentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"


stu1 = Student(90,98,96)
print(stu1.percentage)

stu1.phy = 76
print(stu1.calcPercentage)
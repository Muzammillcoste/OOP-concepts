class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_salary(self):
       return self.pay*12+self.bonus
class Employee:
    def __init__(self,name,age,salary_per):
        self.name=name
        self.age=age
        self.obj_salary=salary_per
    def total_(self):
        return self.obj_salary.annual_salary()
sar1=Salary(50000,10000)
emp1=Employee('muzammil',20,sar1)
print(emp1.total_salary())
        
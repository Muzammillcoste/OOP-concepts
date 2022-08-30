class salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annually_salary(self):
        return self.pay*12+self.pay
class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_salary=salary(pay, bonus)
    def total_salary(self):
        return self.obj_salary.annual_salary()
emp1=Employee('Muzammil',20,50000,10000)
print(emp1.total_salary())
print(emp1.obj_salary.bonus)

#duck typing

class Duck:
    def walk(self):
        print('quack quack')
class Horse:
    def walk(self):
        print('whinny whinny')
class cat:
    def talk(self):
        print('meow meow')
        
def obj_taker_1(obj):
        obj.walk()  #duck typing
        
#you can handle duck typing through this approch
def obj_taker_2(obj):
    if hasattr(obj,'walk'):# 
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
        
h=Horse()
c=cat()
obj_taker_1(h)
obj_taker_2(c)
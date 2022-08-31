#property function allow us to use method as a attribute

class pencil:
    def __init__(self,c='red'):
        self._color=c
    @property
    def color(self):
        'This is a property function '
        return self._color
    @color.setter
    def color(self,c):
        self._color=c
    @color.deleter
    def color(self):
        del self._color
    
a=pencil()
print(a.color)
a.color='green'
print(a.color)
print(help(a))

#same as above but it is now abstractproperty,and if learn about abstraction
#go to abstract.py which is in same repo. 

class pencil(ABC):
    def __init__(self,c='red'):
        self._color=c
        
    @abstractproperty
    def color(self):
        'This is a property function '
        return self._color
    
    @color.setter
    def color(self,c):
        self._color=c
        
    @color.deleter
    def color(self):
        del self._color
        
class child_pencil(pencil):
    color='yellow'
    
a=child_pencil()
print(a.color)
a.color='pink'
print(a.color)

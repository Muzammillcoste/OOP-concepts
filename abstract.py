from abc import ABC,abstractmethod,abstractproperty

# it is comparsary to use abstract method in all child class if it derived from it

class polygon(ABC):
    '''this is an abstract class'''
    @abstractmethod
    def noOfsides(self):
        '''this is an abstract method'''
        print('hahaha')
        
class square(polygon):
    def noOfsides(self):
        super().noOfsides()
        print('I have 4 sides')
        
class rectangle(polygon):
    def noOfsides(self):
        print('I have 4 sides rec')
        
a=square()
a.noOfsides()
b=rectangle()
b.noOfsides()

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,movx,movy):
        self.x+=movx
        self.y+=movy
    def __repr__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'
    def __add__(self,p2):
        return Point(self.x+p2.x,self.y+p2.y)
    def __iadd__(self,p2):
        self.x=self.x+p2.x
        self.y=self.y+p2.y
        return self.x,self.y
point1=Point(4,6)
point2=Point(6,4)
print(point1+point2)
point1+=point2
print(point1)
    


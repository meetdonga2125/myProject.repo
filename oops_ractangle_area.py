#  Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle


class ract():
    
    def __init__(self,length, width):
        self.len = length
        self.wid = width
        
    def ract_area(self):
        print(f'The are of ractangle is {self.len * self.wid}')   
        
        
ract1 = ract(10,20)
ract2 = ract(15,45)

ract1.ract_area()
ract2.ract_area()         
# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle


class circle():
    
    pi = 22/7
    
    def __init__(self,radius):
        self.radius = radius
        
    def cricle_area(self):
        print(f'The area of circle is {self.pi*self.radius**2}')
    
    def circle_perimeter(self):
        print(f'The peremetr of cirlce is {2*self.pi*self.radius}')
        
        
circle1 = circle(14)
circle2 = circle(28)
circle1.cricle_area()
circle1.circle_perimeter() 

circle2.cricle_area()
circle2.circle_perimeter()                   
from math import pi
class Area:
    def area_of_square(self):
        self.side=float(input("Enter side of square: "))
        return self.side**2
    def area_of_rectangle(self):
        self.length=float(input("Enter length of rectangle: "))
        self.breadth=float(input("Enter breadth of rectangle: "))
        return self.length*self.breadth
    def area_of_triangle(self):
        self.base=float(input("Enter base of triangle: "))
        self.height=float(input("Enter height of triangle: "))
        return (0.5*self.base*self.height)
    def area_of_circle(self):
        self.radius=float(input("Enter radius of circle: "))
        return float('%.2f' %(pi*(self.radius**2)))
obj=Area()
while True:
    print('''
          -----------------------------------
          Press 1 to find Area of Square
          Press 2 to find Area of Rectangle
          Press 3 to find Area of Circle
          Press 4 to find Area of Triangle
          Press 5 to Exit
          -----------------------------------
          ''')
    choice=int(input('Enter your choice: '))
    
    if choice==1:
        print('Area of square is:',obj.area_of_square())
    elif choice==2:
        print('Area of rectangle is:',obj.area_of_rectangle())
    elif choice==3:
        print('Area of circle is:',obj.area_of_circle())
    elif choice==4:
        print('Area of triangle is:',obj.area_of_triangle())
    elif choice==5:
        break
    else:
        print('Invalid choice')
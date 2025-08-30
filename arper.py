class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2*3.14 * self.radius 
if __name__== "__main__":
        r=float(input("enter the radius of the circle:"))
        circle=Circle(r)
        print(f"Area:{circle.area():.2f})")
        print(f"peremiter:{circle.area():.2f})")
              

    

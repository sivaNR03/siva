#single inheritance
class vehicle :
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def engine_start(self):
        return "engine started"
class car(vehicle):
    def drive (self):
        return "car is moving" 
mycar=car("BMW","honda")     

print(f"brand:{mycar.brand},model:{mycar.model}")
print(mycar.engine_start())
print(mycar.drive())

#multiple inheritance
class siva:
    def method_siva(self):
        return "method from class siva"
class naga:
    def method_naga(self):
        return "method fom class naga"
class raju(siva,naga):
    def method_raju(self):
        return "method fom class raju"
my_instance = raju()

print(my_instance.method_siva())
print(my_instance.method_naga())        
print(my_instance.method_raju())        

#multilevel inheritance
class animal:
    def speak(self):
        return "animal speaks"


class mammal(animal):
    def feed_milk(self):
        return "mammal feeds milk"


class dog(mammal):
    def bark(self):
        return "dog barks"


my_dog = dog()

print(my_dog.speak())       
print(my_dog.feed_milk())  
print(my_dog.bark())        

#Hierarchical Inheritance
class shape:
    def draw(self):
        return "drawing shape"


class circle(shape):
    def draw_circle(self):
        return "drawing circle"


class square(shape):
    def draw_square(self):
        return "drawing square"
    
circle_instance = circle()
square_instance = square()

print(circle_instance.draw())      
print(circle_instance.draw_circle()) 

print(square_instance.draw())       
print(square_instance.draw_square())

#hybrid inheritance
class Shape:
    def draw(self):
        return "Drawing shape"


class Circle(Shape):
    def draw_circle(self):
        return "Drawing circle"


class Square(Shape):
    def draw_square(self):
        return "Drawing square"


class ColoredShape:
    def set_color(self, color):
        return f"Setting color to {color}"


class ColoredCircle(ColoredShape, Circle):
    def highlight_circle(self):
        return "Highlighting circle"

red_circle = ColoredCircle()
blue_square = Square()

print(red_circle.draw())           
print(red_circle.draw_circle())   
print(red_circle.set_color("red")) 
print(red_circle.highlight_circle())

print(blue_square.draw())        
print(blue_square.draw_square())   
print(blue_square.set_color("blue"))

# Concepts present: classes, f strings, 
from math import sqrt

# Classes can help to describe data that appears in the real world that benefits form being categoriezed .abs(x)
# Arrays are good for homogenous data sets (data that is describing the same thing) like a tempreature matrix
# Classes is good for location informaiton, people, or other real world objects


# Calculating the distance between two points using a class
class Point:
    def __init__ (self, x,y):
        self.x = x
        self.y = y

    
    def distance (self, otherPoint):
        del_x = self.x

# Expressing real and imaginary numbers using a class

class Complex_num:
    def __init__ (self, realPart, imagPart):
        self.real = realPart
        self.imag = imagPart

    
num = Complex_num(3.0, 4.0)

print (num) # this prints off something weird: `<__main__.Complex_num object at 0x000002846BA0FE80>`
print (num.real) # this prints off the real part of the previously defined variable `num`
print (num.imag) # this prints the imaginary part. It seems that `self` will take on the name of new variable declarations. 

num_2 = Complex_num(2.0, -1.20)
print (num_2.real, num_2.imag)


class Driver:
    def __init__(self, implicitly_wait):
        self.implicitly_wait = implicitly_wait

    def get(self, url):
        return f"{url}"


# Create an instance of the Driver class i.e., the object `driver` is created as 
# an object that belongs to the `Driver` class
driver = Driver(900)

url = "https://www.example.com"
driver.get (url)


    
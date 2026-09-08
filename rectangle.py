class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def setHeight(self, h):
        self.height = h

    def setWidth(self, w):
        self.width = w


def area_difference(r1, r2):
    return r1.area() - r2.area()


# Test the Rectangle class
r = Rectangle(5, 4)

area = r.area()
perimeter = r.perimeter()

print("Original rectangle")
print("Width:", r.getWidth())
print("Height:", r.getHeight())
print("Area:", area)
print("Perimeter:", perimeter)


r.setWidth(10)
r.setHeight(15)

area = r.area()
perimeter = r.perimeter()

print()
print("Updated rectangle")
print("Width:", r.getWidth())
print("Height:", r.getHeight())
print("Area:", area)
print("Perimeter:", perimeter)


r1 = Rectangle(10, 10)
r2 = Rectangle(15, 20)

difference = area_difference(r1, r2)

print()
print("Area difference between r1 and r2:", difference)
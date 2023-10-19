class Shap:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY
class Circle(Shap):
    pi = 3.14
    def __init__(self, r = 1, x =0, y = 0):
        Shap.__init__(self, x, y)
        self.r = r
    def area(self):
        return self.r * self.r * self.pi
    def __str__(self):
        return "Circle of radius %s at coordinates (%d, %d)" % (self.r, self.x, self.y)

c1 = Circle()
c2 = Circle(5, 15, 20)
print(c1)
print(c2)
print(c2.area())
c2.move(54, 4)
print(c2)




y = [2, 5, [3, 6, 7, 8, 4]]
print(len(y))
i = 0
while i < len(y):
    print(y[2][i])
    i+=1

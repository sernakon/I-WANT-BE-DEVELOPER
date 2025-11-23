class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

A = Rectangle(10, 20)
B = Rectangle(20, 30)
print(f"S(A){A.height}x{A.width}: {A.calculate_area()} \nS(B){B.height}x{B.width}: {B.calculate_area()}")

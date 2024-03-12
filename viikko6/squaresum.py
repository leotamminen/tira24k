class SquareSum:
    def __init__(self):
        self.y_summa = 0
        self.y_neliosumma = 0
 
        self.x_summa = 0
        self.x_neliosumma = 0
 
        self.yx_summa = 0
        self.n = 0
 
    def add(self, x, y):
        self.y_summa += y
        self.y_neliosumma += y**2
 
        self.x_summa += x
        self.x_neliosumma += x**2
 
        self.yx_summa += y*x
        self.n += 1
 
    def calc(self, a, b):
        h1 = self.y_neliosumma
        h2 = 2 * b * self.y_summa
        h3 = self.n * b**2
        h4 = 2 * a * (self.yx_summa - b * self.x_summa)
        h5 = a**2 * self.x_neliosumma
 
        return (h1 - h2 + h3) - h4 + h5
 
 
 
if __name__ == "__main__":
    s = SquareSum()
    s.add(1, 1)
    s.add(3, 2)
    s.add(5, 3)
    print(s.calc(1, 0)) # 5
    print(s.calc(1, -1)) # 2
    print(s.calc(0.5, 0.5)) # 0 (0.0)
    s.add(4, 2)
    print(s.calc(0.5, 0.5)) # 0.25
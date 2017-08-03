total = 0

class MathDojo():
    def __init__(self):
        pass
    def add(self,a,b):
        global total
        if (isinstance(a, list)):
            a = sum(a)
        if (isinstance(b, list)):
            b = sum(b)
        total += (a+b)
        return self
    def subtract(self,a,b):
        global total
        if (isinstance(a, list)):
            a = sum(a)
        if (isinstance(b, list)):
            b = sum(b)
        total -= (a+b)
        return self
    def result(self):
        global total
        print total
        return self

md = MathDojo().add(2,[3,4,5]).add(2, 5).subtract(3, 2).result()
print md

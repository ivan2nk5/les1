import random


class Cip:
    def __init__(self, *num):
        self.num = num
        self.result = self.calculator()

    def calculator(self):
        result = random.choice(self.num)
        choise_of = [self._add, self._sub, self._mul, self._div]

        for num in self.num:
            operation = random.choice(choise_of)
            result = operation(result, num)

        return result

    def _add(self, a, b):
        return a + b

    def _sub(self, a, b):
        return a - b

    def _mul(self, a, b):
        if a == 0:
            return a
        return a * b

    def _div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("ZeroDivisionError")
            return a

    def __str__(self):
        return f"Result: {self.result}"



cip = Cip(5, 3, 8)
print(cip)

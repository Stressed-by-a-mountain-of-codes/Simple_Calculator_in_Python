class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def calculate(self, a, b, operator):
        if operator not in self.operations:
            raise ValueError(f'Unsupported operation: {operator}')
        return self.operations[operator](a, b)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Division by zero')
        return a / b


if __name__ == '__main__':
    calc = Calculator()
    a = float(input('Enter first number: '))
    op = input('Enter operator (+, -, *, /): ').strip()
    b = float(input('Enter second number: '))
    result = calc.calculate(a, b, op)
    print(f'Result: {result}')





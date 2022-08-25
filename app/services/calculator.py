from app.models.calculator import Calculator


class CalculatorService(object):
    def __init__(self):
        pass

    def calculate(self, first, second):
        calculator = Calculator(first, second)
        print(f'첫번째 숫자 : {calculator.first}')
        print(f'두번째 숫자 : {calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.sum()}')
        print(f'{calculator.first} - {calculator.second} = {calculator.subtraction()}')
        print(f'{calculator.first} * {calculator.second} = {calculator.multip()}')
        print(f'{calculator.first} / {calculator.second} = {calculator.divide()}')
        
        
def read(msg: str)-> int:
    return int(input(f'Enter "{msg}" operand.\n'))


def add():
    num1 = read('x')
    num2 = read('y')
    display('Sum', num1, num2, num1+num2)


def sub()-> int:
    num1 = read('x')
    num2 = read('y')
    display('Difference', num1, num2, num1-num2)


def mul()-> int:
    num1 = read('x')
    num2 = read('y')
    display('Product', num1, num2, num1*num2)


def div()-> int|float:
    num1 = read('x')
    num2 = read('y')
    display('Quotient', num1, num2, num1/num2)


def rem()-> int|float:
    num1 = read('x')
    num2 = read('y')
    display('Remainder', num1, num2, num1%num2)


def display(oper: str, num1: int, num2: int, res: int|float):
    print(f'{oper} of {num1} and {num2} is {res}')
from math import factorial as f

def main():
    num = int(input('Enter a number.\n'))
    if is_strong(num):
        print(f'{num} is strong number.')
    else :
        print(f'{num} isn\'t strong number.')

def main_import(num)-> int:
    if is_strong(num):
        print(f'{num}')
        return 1
    return 0


def is_strong(num: int)-> bool:
    if num == calculate(num):
        return True
    return False


def calculate(num: int)-> int:
    res = 0
    while num:
        digit = digit_retriver(num)
        res += f(digit)
        num = digit_truncate(num)
    return res

def digit_truncate(num: int)-> bool:
    return num//10

def digit_retriver(num: int)-> int:
    return num % 10


if __name__ == '__main__':
    main()
from strong import main_import as m

def main():
    count_needed = int(input('Enter the number of strong numbers neeeded.\n'))
    num = 1
    count= 0
    print('Strong numbers are:')
    while count < count_needed:
        count = add(count, m(num))
        num = add(num, 1)


def add(num1: int, num2: int)-> int:
    return num1 + num2

main()
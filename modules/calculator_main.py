import calculator_work

def main():
    print('\tWelcome to calculator\n')
    select_operation(menu())


def menu()-> str:
    return int(input('Choose opertaion from below:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Remainder\n6. Exit\n'))


def select_operation(choice: int):
    if choice == 6:
        exit()
    if choice == 1:
        calculator_work.add()
    elif choice == 2:
        calculator_work.sub()
    elif choice == 3:
        calculator_work.mul()
    elif choice == 4:
        calculator_work.div()
    elif choice == 5:
        calculator_work.rem()
    else:
        print('\nInvalid choice!!!\n')
        select_operation(menu())

main()
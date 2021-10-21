''' 
main block that uses find_strong to check find strong number(s)
'''
def main() :
    num = int(input('Enter the number of strong numbers needed.\n'))
    print(f'\nFinding {num} strong number(s):')
    if num < 4 :
        find_strong(num)
    else :
        find_strong(4)
    print('Found availabe strong numbers.')
    

# to print specified number of strong numbers
def find_strong(num: int):
    count = 0
    i = 1
    while count < num :
        if is_strong(i) :
            print(i)
            count= add(count, 1)
        i= add(i, 1) 

# is_strong() returns if true or false based on caluclate result from calculate()
def is_strong(num:int)->bool :
    if calculate(num) == num :
        return True
    return False


# does necessary calculation for finding if it is a strong number
def calculate(num:int)->int:
    res = 0
    while num :
        res = add(res,fact(digit_retriver(num)))
        num = num_truncate(num)
    return res


# retrives last digit from number
def digit_retriver(num:int)->int :
    return num % 10


# find factorial of the input number
def fact(num:int)->int :
    fac = 1
    for i in range(1, num+1) :
        fac *= i
    return fac


# truncate number by removing units place in the number
def num_truncate(num:int)->int :
    return num // 10


#simple function to add to number
def add(num1:int, num2:int)->int :
    return num1 + num2


if __name__ == '__main__' :
    main()
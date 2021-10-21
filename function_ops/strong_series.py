''' 
main block that uses is_strong() to check if its strong number
'''
def main() :
    num = int(input('Enter the range.\n'))
    print(f'Strong numbers in the range 1 to {num}')
    for i in range(1, num+1) :
        if is_strong(i) :
            print(f'{i}')
    

# is_strong() returns if true or false based on caluclate result from calculate()
def is_strong(num:int)->bool :
    if calculate(num) == num :
        return True
    return False


# does necessary calculation for finding if it is a strong number
def calculate(num:int)->int:
    res = 0
    while num :
        res += fact(digit_retriver(num))
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


if __name__ == '__main__' :
    main()
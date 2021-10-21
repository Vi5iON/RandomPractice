''' 
main block that uses is_strong() to check if its strong number
'''
def main() :
    num = int(input('Enter the number.\n'))
    if is_strong(num) :
        print(f'{num} is a strong number.')
    else :
        print(f'{num} isn\'t a strong number.')


"""def is_strong(num:int)->bool :
    temp = num
    res = 0
    while temp :
        res += fact(digit_retriver(temp))
        temp = temp_truncate(temp)
    if res == num :
        return True
    return False"""
    

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
    if num :
        return num * fact(num-1)
    return 1


# truncate number by removing units place in the number
def num_truncate(num:int)->int :
    return num // 10


if __name__ == '__main__' :
    main()
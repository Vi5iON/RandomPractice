''' 
main block that uses is_amstrong() to check if its amstrong number
'''
def main() :
    num = int(input('Enter the range.\n'))
    flg = True

    for i in range(1, num+1) :
        if is_amstrong(i) :
            print(i)
            flg = False

    if flg :
        print('No results where found.')


# is_amstrong() returns if true or false based on calculate result from calculate()
def is_amstrong(num: int)->bool :
    if num == calculate(num) :
        return True
    else :
        return False


# does necessary calculation for finding if it is a amstrong number
def calculate(num: int)->int :
    res = 0
    power = num_of_digits(num)
    while num :
        digit = digit_retriver(num)
        res = add(res, digit**power)
        num = num_truncate(num)
    return res


# finds number of digits in the number
def num_of_digits(num: int)->int :
    count = 0
    while num :
        num = num_truncate(num)
        count = add(count,1)
    return count


def add(num1:int, num2:int)->int :
    return num1 + num2


# retrives last digit from number
def digit_retriver(num: int)->int:
    return num % 10


# truncate number by removing units place in the number
def num_truncate(num: int)->int :
    return num // 10


if __name__ == '__main__' :
    main()
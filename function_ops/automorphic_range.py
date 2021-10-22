'''
main block that accepts upper and lower limit.
Finds the automorphic numbers within this range.
EX: 5^2 = 25, 25^2 = 625
'''
def main() :
    lower = int(read('Enter the lower range.\n'))
    upper = int(read('Enter the upper range.\n'))
    print(f'\nAutomorphic numbers within the range ({lower},{upper}) are:')
    for i in range(lower, upper) :
        if is_automorphic(i) :
            print(i)


#checks if the given number is automorphic
def is_automorphic(num: int)->bool :
    sqr = squr(num)
    while num :
        if digit_retriever(num) != digit_retriever(sqr) :
            return False
        num = num_truncate(num)
        sqr = num_truncate(sqr)
    return True


#returns remainder
def digit_retriever(num: int)->int :
    return num % 10


#removes the unit place of the number, truncates it
def num_truncate(num: int)->int :
    return num // 10


#finds square of the number
def squr(num) :
    return int(num**2)


#simply read user input
def read(msg: str)->str :
    return input(msg) 


if __name__ == '__main__' :
    main()
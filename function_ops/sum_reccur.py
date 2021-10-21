def main () :
    print(f'\nSum of 1st 10 numbers is {sumer(10)}')

def sumer(num:int )->int :
    if num :
        return num + sumer(num-1)
    return 0

if __name__ == '__main__' :
    main()
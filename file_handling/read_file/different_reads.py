def hand_read():
    '''hand_read'''
    print(hand_read.__doc__)
    handle = open('D:\PythonCodes\\file_handling\\random_file.txt')
    print(handle.read())


def for_read():
    '''for_read'''
    print(for_read.__doc__)
    handle = open('D:\PythonCodes\\file_handling\\random_file.txt')
    for line in handle:
        print(line, end='')
    print()

    
def while_read():
    '''while_read'''
    print(while_read.__doc__)
    handle = open('D:\PythonCodes\\file_handling\\random_file.txt')
    data = handle.readline()
    while data:
        print(data, end='')
        data = handle.readline()


hand_read()
print()

for_read()
print()

while_read()
print()
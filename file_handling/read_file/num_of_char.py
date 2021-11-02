def main():
    handle = open('D:\PythonCodes\\file_handling\\hello.txt')
    print(handle.read())
    print(f'Number of characters in strings is {handle.tell()}\n')
    handle.seek(0)
    total = 0
    data = handle.readline()
    while data:
        print(data, end='')
        print(char_per_line(data))
        total += char_per_line(data) + 1
        data = handle.readline()

    print(f'\nTotal characters in file by counting {total}')
        


def char_per_line(string):
    return len(string)

main()
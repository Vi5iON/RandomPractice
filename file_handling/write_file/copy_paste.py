def main():
    print('Start!!\n')

    handle_read = open('D:\PythonCodes\\file_handling\\random_file.txt')
    read_string = handle_read.read()
    handle_read.close()

    handle_write = open('D:\PythonCodes\\file_handling\\written.txt', 'w')
    handle_write.write(read_string)
    handle_write.flush()
    handle_write.close()

    print('Done!!')


main()
def main():
    handle = open('D:\PythonCodes\\file_handling\\leave.txt','w')
    string = 'Leave from 4th for 4 days.'

    handle.write(string)
    handle.flush()
    print('done')
    handle.close()

    handle = open('D:\PythonCodes\\file_handling\\leave.txt','a')
    string = '\nEnjoy!!'
    handle.write(string)
    handle.flush()
    print('done')
    
main()
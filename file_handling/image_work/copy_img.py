def main():
    print('Start!')
    handle_main = open('D:\PythonCodes\\file_handling\\image_work\\one_piece.png', 'rb')
    img = handle_main.read()
    handle_main.close()
    
    create_png(img)
    create_jpeg(img)
        
    print('End!')


def create_png(img: bytes):    
    handle = open('D:\PythonCodes\\file_handling\\image_work\\one_piece_copy_PNG.png', 'wb')
    handle.write(img)
    handle.close()
    print('png file created.\n')


def create_jpeg(img: bytes):
    handle = open('D:\PythonCodes\\file_handling\\image_work\\one_piece_copy_JPEG.jpeg', 'wb')
    handle.write(img)
    handle.close()
    print('jpeg file created.\n')

if __name__ == '__main__':
    main()
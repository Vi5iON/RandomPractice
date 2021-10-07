#find if given number is divisible or not

num_to_be_checked = int(input('Enter the number to be checked.\n'))
num_checker = int(input('Enter the checker.\n'))

# using tif
#print(str(num_to_be_checked)+' is a multiple of '+str(num_checker) if num_to_be_checked % num_checker == 0 else str(num_to_be_checked)+' is\'nt a multiple of '+str(num_checker))

if num_to_be_checked % num_checker == 0 :
    print(num_to_be_checked,'is a multiple of', num_checker)
else :
    print(num_to_be_checked,'is\'nt a multiple of', num_checker)
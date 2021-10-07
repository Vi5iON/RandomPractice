# provide gardes to the input marks.

print('Welcome to grade provider.\n')

marks = float(input('Enter the marks of the student.\n'))

# checking with grade range the marks belong too.

if marks >= 90 :
    print('A grade.')
elif 90 > marks >= 80 :
    print('B grade.')
elif 80 > marks >= 70 :
    print('C grade.')
elif 70 > marks >= 60 :
    print('D grade.')
elif 60 > marks >= 50 :
    print('E grade.')
else :
    print('Fail.')
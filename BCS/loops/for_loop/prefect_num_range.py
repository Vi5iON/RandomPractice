num = int(input('Enter a range.\n'))

#finding factors and suming them

for i in range(1, num+1) :
    res = 0
    for j in range(1, i) :
        if i % j == 0 :
            res += j
    if res == i :
        print(i, 'is a perfect number.\n')
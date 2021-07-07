Input = input("Enter a number: ")
factorial = 1
if int(Input) >= 1:
    for i in range (1,int(Input)+1):
        factorial = factorial * i
n = 0
for i in str(factorial)[::-1]:
    if(i == '0'):
        n+=1
    else:
        break

print('{} has {} trailing zeros.'.format(factorial,n))
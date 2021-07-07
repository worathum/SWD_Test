Input = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    Input.append(int(input()))
    
max = Input[0]
output = 0
for idx, val in enumerate(Input):
    if(val>max):
        output,max = idx,val
print('Your list: {}'.format(Input))
print('The index of the max value in your list = {}'.format(output))
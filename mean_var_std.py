import numpy as np

def calculate(list):
    matrix = np.array(list).reshape(3,3)
    # calculating the mean
    mean_axis1 = np.mean(matrix, axis = 1)
    mean_axis2 = np.mean(matrix, axis = 0)   
    mean_flattened = np.mean(matrix)
     #calculating the variance

     



    return calculations
x = []
y = int(input('Please enter a list of 9 numbers:'))
if y == len(9):
    for i in range (y):
        ele = int(input())
        x.append(ele)
else:
    print('Value Error: list must contain 9 numbers')

calculations = calculate(y)
print(calculations)



    

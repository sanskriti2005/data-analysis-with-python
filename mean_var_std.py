import numpy as np

def calculate(list):
    matrix = np.array(list).reshape(3,3)
    # calculating the mean
    mean_axis1 = np.mean(matrix, axis = 1)
    mean_axis2 = np.mean(matrix, axis = 0)   
    mean_flattened = np.mean(matrix)
    
     #calculating the variance
     var_axis1 = np.var(matrix, axis = 1)
     var_axis2 = np.var(matrix, axis = 0)
     var_flattened = np.var(matrix)

     #CALCULATING THE STANADARD DEVIATION
     std_axis1 = np.std(matrix, axis = 1)
     std_axis2 = np.std(matrix, axis = 0)
     std_flattened = np.std(matrix)

     #CALCULATING THE MAX
     max_axis1 = max(matrix, axis = 1)
     max_axis2 = max(matrix, axis = 0)
     max_flattened = max(matrix)

     #CALCULATING THE MIN
     min_axis1 = min(matrix, axis = 1)
     min_axis2 = min(matrix, axis = 0)
     min_flattened = min(matrix)
     

     



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



    

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

     #CALCULATING THE SUM 
     sum_axis1 = sum(matrix, axis = 1)
     sum_axis2 = sum(matrix, axis = 0)
     sum_flattened = sum(matrix)


    calculations = { 'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [var_axis1, var_axis2, var_flattened],
        'standard_deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened] }



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



    

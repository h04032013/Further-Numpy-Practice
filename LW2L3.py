import numpy as np

#1.2 Solving using matrix

#Matrix
A = np.array([[4,-3,1],
              [2,1,3],
              [-1,2,-5]], dtype= np.dtype(float))

b = np.array([-10,0,17], dtype=float) 

print(f'Matrix A: \n{A}')
print(f'\nArray b: \n{b}')

#Finding sigularity and determinant
s = ''
d = np.linalg.det(A)

if d != 0:
    s = 'Non Singular'
else:
    s = 'Singular'

print(f'\nSigularity: {s} \nDeterminant of A: {d:.1f}')

#Solving the system
x = np.linalg.solve(A,b)
print(f'\nSolution: {x}')

# 2.1 Preparing for Row Reduction
A_sys = np.hstack( (A,b.reshape( (3,1 ))) )

print(A_sys)

# 2.2 Operations as functions
def MultiplyRow (M, row, row_mult):
    M_new = M.copy()
    M_new[row] = M_new[row] * row_mult
    return M_new

print(f'Original Matrix: \n{A_sys}')
print(f'Matrix after Row 3 x2: \n{MultiplyRow(A_sys,2,2)}')

# multiply row1 by row1_mult and add it to the row2, 
# exchanging row2 of the matrix M in the result
def AddRows(M, row_num_1, row_num_2, row_num_1_multiple):
    M_new = M.copy()
    M_new[row_num_2] = row_num_1_multiple * M_new[row_num_1] + M_new[row_num_2]
    return M_new

print("Original matrix:")
print(A_sys)
print("\nMatrix after exchange of the third row with the sum of itself and second row multiplied by 1/2:")
print(AddRows(A_sys,1,2,1/2))

#Swap Rows
def SwapRows(M, row1, row2):
    M_new = M.copy
    
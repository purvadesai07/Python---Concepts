A = [[1, 10], [2,20]]
B = [[3, 30], [4,40]]
result = [[0, 0], [0,0]]
result1 = [[0,0], [0,0]]
transpose = [[0,0], [0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
        result1[i][j] = A[i][j] - B[i][j]
print("Addition Result: ", result)
print("Subtraction Result: ", result1)
for i in range(len(A)):
    for j in range(len(A[0])):
        transpose[i][j] = A[j][i]
print("Transpose: ", transpose)
if A == transpose:
    print("The matrix is symmetric!")
else:
    print("The matrix is not symmetric.")
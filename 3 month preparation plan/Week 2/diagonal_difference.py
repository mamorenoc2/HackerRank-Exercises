'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17 . Their absolute difference is |15 - 17| = 2.

Function description

Complete the diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
'''
def diagonalDifference(arr):
    n = len(arr)
    left_diagonal = 0
    right_diagonal = 0
    for i in range(n):
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][n - 1 - i] 
    
    absolute_sum = abs(left_diagonal - right_diagonal)
    return absolute_sum


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
print(diagonalDifference(arr)) 
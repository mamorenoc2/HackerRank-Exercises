'''
     Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
arr = [1, 3, 5, 7, 9]
The minimum sum is 1 + 3 + 5 + 7 and the maximum sum is 3 + 5 + 7 + 9. The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of 5 integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5
Sample Input

1 2 3 4 5
Sample Output

10 14 elements.
'''

def min_max_sum(arr):
    arr.sort()

    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])

    print(min_sum, max_sum)

arr = [1, 2, 3, 4, 5]

min_max_sum(arr)
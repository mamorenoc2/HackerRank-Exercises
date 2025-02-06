'''
Given an array of integers and a positive integer k, determine the number of (i, j) pairs when
i < j and ar[i] + ar[j] is divisible for k

Example
arr = [1,2,3,4,5,6]
k=5
Three pairs meet the criteria: [1,4], [2,3]  and [4,6].

Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

int n: the length of array 
int ar[n]: an array of integers
int k: the integer divisor
Returns
- int: the number of pairs

Sample Input

STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
Sample Output

 5

'''

def divisible_sum_pairs(n, k, arr):
    count = 0
    # Recorrer todos los pares (i, j) donde i < j
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    
    return count

arr = [1, 3, 2, 6, 1, 2]
n = 6
k = 3
print(divisible_sum_pairs(n, k, arr))

'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example
arr = [1, 1, 0, -1, -1]
There are n = 5  elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000, 1/5 = 0.200000,  and . Results are printed as:

0.400000
0.400000
0.200000

Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.


Sample Input
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output

0.500000
0.333333
0.166667

'''

def PlusMinus(arr):
    len_arr = len(arr)
    n_positive = 0
    n_negative = 0
    n_zero = 0

    for number in arr:
        if number > 0:
            n_positive +=1
        elif number < 0:
            n_negative += 1
        else:
            n_zero += 1
    
    positive_ratio = n_positive / len_arr
    negative_ratio = n_negative / len_arr
    zero_ratio = n_zero / len_arr

    print("{0:.6f}".format(positive_ratio))
    print("{0:.6f}".format(negative_ratio))
    print("{0:.6f}".format(zero_ratio))


arr = [-4, 3, -9, 0, 4, 1]
PlusMinus(arr)

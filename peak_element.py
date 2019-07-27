# Given an array A of N integers. The task is to find a peak element in it.
# An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.

# Note: There may be multiple peak element possible, in that case you may return any valid index.

# Input Format:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N. Then in the next line are N space separated values of the array.

# Output Format:
# For each test case output will be 1 if the index returned by the function is an index with peak element.

# User Task:
# You don't have to take any input. Just complete the provided function peakElement() and return the valid index.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 1 <= A[] <= 1000

# Example:
# Input:
# 2
# 3
# 1 2 3
# 2
# 3 4
# Output:
# 1
# 1

# Explanation:
# Testcase 1: In the given array, 3 is the peak element.
# Testcase 2: 4 is the peak element.


t = int(input())


def peak_element(arr, n):
    if(n == 1):
        return 0
    for j in range(1, n-1):
        if(arr[j] > arr[j-1] and arr[j] > arr[j+1]):
            return j
    if(arr[0] > arr[1]):
        return 0
    if(arr[n-1] > arr[n-2]):
        return n-1


for i in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = peak_element(arr, n)
    if x:
        print("1")

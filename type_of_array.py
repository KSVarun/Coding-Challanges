# You are given an array of size N having no duplicate elements. The array can be categorized into following:
# 1.  Ascending
# 2.  Descending
# 3.  Descending Rotated
# 4.  Ascending Rotated
# Your task is to print which type of array it is and the maximum element of that array.

# Input:
# The first line of input contains an integer T denoting the no test cases. Then T test caes follow. Each testcase contains two lines of input. The first line contains an integer N denoting the size of the array. The next line contains N space separated values of the array.

# Output:
# For each test case, print the largest element in the array and and integer x denoting the type of the array.

# Constraints:
# 1 <= T <= 100
# 3 <= N <= 107
# 1 <= A[] <= 1018

# Example:
# Input:
# 2
# 5
# 2 1 5 4 3
# 5
# 3 4 5 1 2

# Output:
# 5 3
# 5 4

# Explanation:
# Testcase1:
# Input : A[] = { 2, 1, 5, 4, 3}
# Output : Descending rotated with maximum element 5
# Testcase2:
# Input : A[] = { 3, 4, 5, 1, 2}
# Output : Ascending rotated with maximum element 5

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 0
    for j in range(0, n-2):
        if arr[j] < arr[j+1]:
            flag = 1
        elif arr[j] > arr[j+1]:
            flag = 2

    print(max(arr), end=' ')
    print(flag)

# 2nd sol

    n = int(input())
    l = list(map(int, input().split()))
    m = max(l)
    l2 = sorted(l)

    if l2 == l:
        print(m, 1)
    elif l2 == l[::-1]:
        print(m, 2)
    elif l[-1] > l[0]:
        print(m, 3)
    else:
        print(m, 4)

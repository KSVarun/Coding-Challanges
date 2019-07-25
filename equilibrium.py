# Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array. Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Input:
# The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. First line of each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array A.

# Output:
# For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium point exists print -1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 106
# 1 <= Ai <= 108

# Example:
# Input:
# 2
# 1
# 1
# 5
# 1 3 5 2 2

# Output:
# 1
# 3

# Explanation:
# Testcase 1: Since its the only element hence its the only equilibrium point.
# Testcase 2: For second test case equilibrium point is at position 3 as elements below it (1+3) = elements after it (2+2).


t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if(n == 1):
        print(*arr)
        exit()
    else:
        left = 1
        right = 2
        mid = 1
        while mid != n-2:
            suml = 0
            sumr = 0
            for j in range(0, left):
                suml = suml+arr[j]
            for k in range(right, n):
                sumr = sumr+arr[k]
            mid = mid+1
            left = left+1
            right = right+1
            if suml == sumr:
                print(mid)
                exit()
        print("-1")


# second sol   sweet logic prev_sum ==(total_sum-arr[i]-prev_sum)
        t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        arr = [int(x) for x in arr]
        total_sum = sum(arr)

        prev_sum = 0
        flag = False
        for i in range(n):
            if prev_sum == (total_sum-arr[i]-prev_sum):
                print(i+1)
                flag = True
                break
            else:
                prev_sum += arr[i]

        if flag == False:
            print(-1)

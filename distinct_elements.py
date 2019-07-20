# Given an array A[] of size N and an integer K. Your task is to complete the function countDistinct() which prints the count of distinct numbers in all windows of size k in the array A[].

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two integers N and K. Then in the next line are N space separated values of the array A[].

# Output:
# For each test case in a new line print the space separated values denoting counts of distinct numbers in all windows of size k in the array A[].

# Constraints:
# 1 <= T <= 100
# 1 <= N, K <= 100
# 1 <= A[] <= 100

# Example(To be used only for expected output):
# Input:
# 2
# 7 4
# 1 2 1 3 4 2 3
# 3 2
# 4 1 1

# Output:
# 3 4 4 3
# 2 1


t = int(input())

for i in range(t):
    N, k = map(int, input().strip().split())
    arr = list(map(int, input().split()))
    first_index = 0
    last_index = k
    iter = N-k
    ans = []
    for k in range(0, iter+1):
        distinct = []
        for j in range(first_index, last_index):
            if arr[j] not in distinct:
                distinct.append(arr[j])
        ans.append(len(distinct))
        first_index += 1
        last_index += 1
    print(*ans)

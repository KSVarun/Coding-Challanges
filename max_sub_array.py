

# Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

# Input:
# The first line of input contains an integer T denoting the number of test cases. The first line of each test case contains a single integer N denoting the size of array and the size of subarray K. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

# Output:
# Print the maximum for every subarray of size k.

# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 107
# 1 ≤ K ≤ N
# 0 ≤ A[i] <= 107

# Example:
# Input:
# 2
# 9 3
# 1 2 3 1 4 5 2 3 6
# 10 4
# 8 5 10 7 9 4 15 12 90 13

# Output:
# 3 3 4 5 5 5 6
# 10 10 10 15 15 90 90

# Explanation:
# Testcase 1: Starting from first subarray of size k = 3, we have 3 as maximum. Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6

t = int(input())

for i in range(t):
    N, k = map(int, input().strip().split())
    arr = list(map(int, input().split()))
    first_index = 0
    last_index = k
    iter = N-k
    ans = []
    for k in range(0, iter+1):
        max = 0
        for j in range(first_index, last_index):
            if arr[j] > max:
                max = arr[j]
        ans.append(max)
        first_index += 1
        last_index += 1
    print(*ans)


# second TLE less soln

for x in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    queue = []
    m = 0
    for i in a:
        if len(queue) == k:
            val = queue.pop(0)
            queue.append(i)
            print(m, end=' ')
            if val == m:
                m = max(queue)
            else:
                if m < i:
                    m = i
        else:
            if m < i:
                m = i
            queue.append(i)
    print(m)

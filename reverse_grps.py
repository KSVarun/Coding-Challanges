# Example:
# Input
# 2
# 5 3
# 1 2 3 4 5
# 6 2
# 10 20 30 40 50 60

# Output
# 3 2 1 5 4
# 20 10 40 30 60 50

# Explanation:
# Testcase 1: Reversing groups in size 3, first group consists of elements 1, 2, 3. Reversing this group, we have elements in order as 3, 2, 1.

t = int(input())


def cal_reverse(N, S, arr, E, C, A):
    for j in range(S, E, -1):
        rev.append(arr[j])
    C -= 1
    E = S
    S = (S+A)
    if(C != 0 | 0 < C):
        return cal_reverse(N, S, arr, E, C, A)
    elif(E != (N-1)):
        S = N - 1
        return cal_reverse(N, S, arr, E, C, A)
    return


for i in range(t):
    N, S = input().split(" ")
    N = int(N)
    S = int(S)
    A = S
    E = -1
    C = N//S
    S -= 1
    rev = []
    arr = list(map(int, input().split(" ")))
    cal_reverse(N, S, arr, E, C, A)
    print(*rev)


# super solution
    t = int(input())
for t_itr in range(t):
    n, x = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]

    for i in range(n // x + 1):
        #print(x * (i + 1) - 1, x * i - 1)
        for j in range(x * (i + 1) - 1, x * i - 1, -1):
            if(j < n):
                print(arr[j], end=" ")

    print()

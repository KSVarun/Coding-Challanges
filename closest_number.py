# Example:
# Input:
# 2
# 4 4
# 1 3 6 7
# 7 4
# 1 2 3 5 6 8 9

# Output:
# 3


t = int(input())

small = 0


def cal(arr, num):
    for i in range(len(arr)-1, 0, -1):
        x = num - arr[i]
        xu = (num - arr[i-1])
        if(abs(xu) < abs(x)):
            small = arr[i-1]
        elif(abs(xu) == abs(x)):
            small = arr[i]
        elif(abs(x) < abs(xu)):
            small = arr[i]
            return small

    return small


for i in range(t):
    N, num = [int(i) for i in input().split()]
    arr = list(map(int, input().split()))
    val = cal(arr, num)
    print(val)

# 2nd sol

for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    k = 0
    l = list(map(int, input().strip().split()))
    if(m in l):
        print(m)
    else:
        for k in range(0, n):
            if(l[k] > m):
                break
        if(k == 0):
            print(l[k])
        elif(l[k]-m <= m-l[k-1]):
            print(l[k])
        else:
            print(l[k-1])

t = int(input())

for i in range(0, t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    large = 0
    flag = 0
    index = 0
    for j in range(0, n):
        if(arr[j] > k):
            large = arr[j]
            break
    for j in range(0, n):
        if(arr[j] <= k and arr[j] <= large):
            flag = 1
            index = j
    if(flag == 0):
        print("-1")
    else:
        print(index)

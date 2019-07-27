t = int(input())

for i in range(0, t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    for j in range(0, n):
        if(arr[j] == x):
            count = count+1

    if(count == 0):
        print("-1")
    else:
        print(count)

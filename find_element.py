t = int(input())

for i in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    for j in range(0, n):
        if(k == arr[j]):
            print(j)
            exit()
    print("-1")

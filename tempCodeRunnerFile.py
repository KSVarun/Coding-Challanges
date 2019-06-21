
t = int(input())

while(t > 0):
    n = int(input())
    arr = list(map(int, (input().split())))
    d = int(input())
    brr = [0]*(n)
    for i in range(0, n):
        k = n-d+i
        if (k >= n):
            k = k-n
        brr[k] = arr[i]
    for i in range(n):
        print(brr[i], end=" ")
    print()

    t -= 1

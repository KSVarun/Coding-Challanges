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

t = int(input())

for i in range(t):
    na = int(input())
    arr_a = list(map(int, input().split()))
    nb = int(input())
    arr_b = list(map(int, input().split()))
    for j in range(0, na-1):
        diff = 0
        diff1 = abs(arr_a[j]-arr_a[j+1])
        if

t = int(input())
for i in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    first = 0
    last = 0
    for j in range(0, n):
        if(arr[j] == k):
            first = j
            break
    for l in range(first, n):
        if(arr[l] == k):
            last = l
    if(last == 0):
        last = first
    if(last == 0 and first == 0):
        print("-1")
    else:
        print(str(first)+" "+str(last))

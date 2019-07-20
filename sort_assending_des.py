t = int(input())


for i in range(t):
    even = []
    odd = []
    ans = []
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if(arr[i] % 2 == 0 or arr[i] == 0):
            even.append(arr[i])
        elif(arr[i] % 2 != 0):
            odd.append(arr[i])
    odd.sort(reverse=True)
    even.sort()
    ans = odd
    for i in range(len(even)):
        ans.append(even[i])
    print(*ans)

t = int(input())
for i in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-2])

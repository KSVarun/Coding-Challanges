t = int(input())

for i in range(0, t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    for j in range(0, n):
        if(arr1[j] not in arr2):
            print(j)

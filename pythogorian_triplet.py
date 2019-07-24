t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    squared_arr = []
    for j in arr:
        squared_arr.append(j*j)
    squared_arr.sort()
    fi = 0
    for k in range(fi, n):
        for l in range(fi+1, n):
            pythogors = squared_arr[k] + squared_arr[l]
            if(pythogors <= squared_arr[n-1]):
                if(pythogors in squared_arr):
                    print("Yes")
                    exit()

    print("No")

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if(n == 1):
        print(*arr)
        exit()
    else:
        left = 1
        right = 2
        mid = 1
        while mid != n-2:
            suml = 0
            sumr = 0
            for j in range(0, left):
                suml = suml+arr[j]
            for k in range(right, n):
                sumr = sumr+arr[k]
            mid = mid+1
            left = left+1
            right = right+1
            if suml == sumr:
                print(mid)
                exit()
        print("-1")


# second sol   sweet logic prev_sum ==(total_sum-arr[i]-prev_sum)
        t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        arr = [int(x) for x in arr]
        total_sum = sum(arr)

        prev_sum = 0
        flag = False
        for i in range(n):
            if prev_sum == (total_sum-arr[i]-prev_sum):
                print(i+1)
                flag = True
                break
            else:
                prev_sum += arr[i]

        if flag == False:
            print(-1)

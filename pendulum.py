# Example:
# Input:
# 2
# 5
# 1 3 2 5 4
# 5
# 11 12 31 14 5

# Output:
# 5 3 1 2 4
# 31 12 5 11 14

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0]*n
    mid = n//2
    if n % 2 == 0:
        mid = (n-1)//2
    right = 0
    left = 0
    for i in range(1, len(arr)+1):
        min_ = min(arr)
        arr.remove(min_)
        if i % 2 == 0:
            ans[mid+right] = min_
            left = left-1
        else:
            ans[mid+left] = min_
            right = right+1
    print(*ans)

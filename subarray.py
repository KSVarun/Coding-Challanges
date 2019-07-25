t = int(input())


def subarr(n, sum, arr):
    fi = 0

    flag = 0
    while flag == 0:
        sumf = 0
        for j in range(fi, n):
            sumf = sumf+arr[j]
            if(sumf == sum):
                print(str(fi+1)+" "+str(j+1))
                flag = 1
                exit()
            if(sumf > sum):
                break
        fi = fi+1

    return False


for i in range(t):
    n, sum = map(int, input().split())
    arr = list(map(int, input().split()))
    x = subarr(n, sum, arr)
    if x == False:
        print("-1")

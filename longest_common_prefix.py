t = int(input())

for i in range(0, t):
    n = int(input())
    length_arr = []
    arr = list(map(str, input().split()))
    for i in range(0, n):
        length_arr.append(len(arr[i]))
    ran = min(length_arr)
    l = 1
    ele = arr[1]
    for i in range(0, ran):
        prefix = ele[:l]
        for j in range(1, n):
            elej = arr[j]
            if(prefix != elej[:l]):
                prefix = elej[:l-1]
                print(prefix)
                break
        l = l+1

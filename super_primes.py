t = int(input())
for i in range(0, t):
    n = int(input())
    prime = [1, 2, 3]
    count = 0
    counted = []
    for j in range(4, n+1):
        for k in range(2, n+1):
            if(j > k):
                if(j % k == 0 and j != k):
                    flag = 1
                    break
            elif(j <= k):
                flag = 0
                break
        if(flag == 0):
            prime.append(j)

    for l in range(0, len(prime)):
        for m in range(1, len(prime)):
            sum = prime[l]+prime[m]
            if(sum in prime and sum not in counted):
                counted.append(sum)
    print(prime)
    print(counted)
    print(len(counted))

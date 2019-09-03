# Given two arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.

# Input:
# The first line consists of a single integer T, the number of test cases. For each test case, the first line contains 2 integers n & m denoting the size of two arrays. Next line contains n- space separated integers denoting the elements of array A and next lines contains m space separated integers denoting the elements of array B followed by an integer x denoting the number whose closest sum is to find.

# Output:
# For each test case, the output is 2 space separated integers whose sum is closest to x.

# Constraints:
# 1<=T<=100
# 1<=n,m<=50
# 1<=A[i],B[i]<=500

# Example:
# Input:
# 2
# 4 4
# 1 4 5 7
# 10 20 30 40
# 32
# 4 4
# 1 4 5 7
# 10 20 30 40
# 50
# Output:
# 1 30
# 7 40

t = int(input())
for i in range(0, t):
    n1, n2 = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    k = int(input())
    arr1.sort()
    arr2.sort()
    arr3 = []
    arr4 = []

    if(arr1[n1-1] + arr2[n2-1] <= k):
        print(str(arr1[n1-1]) + " "+str(arr2[n2-1]))
    else:

        large = 0
        largef = 0
        for j in range(0, n1):
            for l in range(0, n2):
                sum = 0
                large1 = large
                sum = arr1[j]+arr2[l]
                large = sum

                if(sum > k and large1 <= k):
                    arr3.append(arr1[j])
                    arr3.append(arr2[l-1])
                    arr4.append(arr3)
                    arr3 = []
        # for m in range(0, len(arr4)):
        for m in range(0, len(arr4)):
            sumf = 0
            large1f = largef
            sumf = arr4[m][0]+arr4[m][1]
            largef = sumf
            if(large1f <= k and large1f >= sumf):
                print(arr4[m-1])


# 2nd best soln
for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    arrn = [int(i) for i in input().split()]
    arrm = [int(i) for i in input().split()]
    x = int(input())
    diff = 5000
    arrn.sort()
    arrm.sort()
    for nn in range(n):
        for mm in range(m):
            s = arrn[nn]+arrm[mm]
            d = abs(x-s)
            if d < diff:
                diff = d
                ans1 = arrn[nn]
                ans2 = arrm[mm]
    print(ans1, ans2)

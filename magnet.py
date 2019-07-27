# Given n Magnets which are placed linearly, with each magnet to be considered as of point object. Each magnet suffers force from its left sided magnets such that they repel it to the right and vice versa. All forces are repulsive. The force being equal to the distance (1/d , d being the distance). Now given the positions of the magnets, the task to find all the points along the linear line where net force is ZERO.

# Note: Distance have to be calculated with precision of 0.0000000000001.

# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The second line of each test case contains an integer N. Then in the next line are N space separated values of the array M[], denoting the positions of the magnet.

# Output:
# For each test case in a new line print the space separated points having net force zero till precised two decimal places.

# Constraints:
# 1<=T<=100
# 1<=N<=100
# 1<=M[]<=1000

# Example:
# Input:
# 2
# 2
# 1 2
# 4
# 0 10 20 30
# Output:
# 1.50
# 3.82 15.00 26.18


t = int(input())
while(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    for i in range(n-1):
        x = arr[i]+(arr[i+1]-arr[i])/2
        l = arr[i]
        r = arr[i+1]
        k = 0
        while(r-l > 0.000001):
            suml = 0
            sumr = 0
            for j in range(i+1):
                suml = suml+1/(x-arr[j])
            for j in range(i+1, n):
                sumr = sumr+1/(arr[j]-x)
            if(suml > sumr):
                l = x
                x = x+(r-l)/2
            elif(suml < sumr):
                r = x
                x -= (r-l)/2
            else:
                break
        print("%.2f" % (x), end=" ")
        # exit(0)
    print()
    t -= 1


# 2nd soln
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        low = a[i]
        high = a[i+1]
        while (abs(low-high) > 0.0000001):
            mid = (low+high)/2
            force = 0
            for j in range(i+1):
                force += 1/(mid-a[j])
            for j in range(i+1, n):
                force -= 1/(a[j]-mid)
            if (force > 0):
                low = mid
            elif (force < 0):
                high = mid
            else:
                break
        print('%.2f' % mid, end=" ")
    print()

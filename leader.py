# Example:
# Input:
# 3
# 6
# 16 17 4 3 5 2
# 5
# 1 2 3 4 0
# 5
# 7 4 5 7 3
# Output:
# 17 5 2
# 4 0
# 7 7 3

# Explanation:
# Testcase 3: All elements on the right of 7 (at index 0) are smaller than or equal to 7. Also, all the elements of right side of 7 (at index 3) are smaller than 7. And, the last element 3 is itself a leader since no elements are on its right.


t = int(input())


def cal_leader(N, arr):
    leader = []
    for k in range(N):
        flag = 0
        e = int(arr[k])
        #print("element "+str(e))
        for j in range(k+1, N):
            #print("arr[j] "+arr[j])
            if(e >= int(arr[j])):
                #print("flag "+str(flag))
                flag = 1
                #print("after flag"+str(flag))
            else:
                flag = 0
                break
        if(flag == 1):
            leader.append(e)
            # print(leader)

    leader.append(int(arr[N-1]))
    print(*leader)


for i in range(t):
    N = int(input())
    arr = input().split(" ")
    # print(arr)
    cal_leader(N, arr)


# second super logic
n = int(input())
l1 = []
s = " "
l = list(map(int, input().split()))
a = l[len(l)-1]
print("a "+str(a))
for i in range(len(l)-1, 0, -1):
    if l[i-1] >= a:
        print("lll "+str(l[i-1]))
        l1.append(l[i-1])
        print(l1)
        a = l[i-1]
        print("a after"+str(a))
l1 = l1[::-1]

l1.append(l[len(l)-1])
print(*l1)

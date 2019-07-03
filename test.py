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

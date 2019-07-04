

# t = int(input())


# def cal_leader(N, arr):
#     leader = []
#     for k in range(N):
#         flag = 0
#         e = int(arr[k])
#         #print("element "+str(e))
#         for j in range(k+1, N):
#             #print("arr[j] "+arr[j])
#             if(e >= int(arr[j])):
#                 #print("flag "+str(flag))
#                 flag = 1
#                 #print("after flag"+str(flag))
#             else:
#                 flag = 0
#                 break
#         if(flag == 1):
#             leader.append(e)
#             # print(leader)

#     leader.append(int(arr[N-1]))
#     print(*leader)


# for i in range(t):
#     N = int(input())
#     arr = input().split(" ")
#     # print(arr)
#     cal_leader(N, arr)

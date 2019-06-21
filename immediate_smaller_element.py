test_cases = int(input())
input_count = 0
array_list = []
i = 0
j = 0
k = 0


def immediate_small(array_list, array_length):
    for k in range(array_length):
        try:
            if(array_list[k+1] < array_list[k]):
                print(array_list[k+1])
            else:
                print(-1)
        except:
            print(-1)
    return


for i in range(test_cases):
    array_length = int(input())
    array_list = []
    for j in range(array_length):
        array_list.append(int(input()))
    immediate_small(array_list, array_length)

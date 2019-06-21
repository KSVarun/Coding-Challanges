test_cases = int(input())
input_count = 0
array_list = []
i = 0
j = 0
k = 0


def immediate_small(array_list, array_length):
    output_array = []
    for k in range(array_length):
        try:
            if(int(array_list[k+1]) < int(array_list[k])):
                #print(int(array_list[k+1]), sep=' ')
                output_array.append(int(array_list[k+1]))
            else:
                #print(-1, sep=' ')
                output_array.append(int(-1))
        except:
            #print(-1, sep=' ')
            output_array.append(int(-1))
    print(*output_array)
    return


for i in range(test_cases):
    array_length = int(input())
    array_list = []
    array_input = input()
    array_list = array_input.split(" ")
    # for j in range(array_length):
    #    array_list.append(int(input()))
    immediate_small(array_list, array_length)

# first partial sollution according to onine gfg compiler

test_cases = int(input())
#array_length = 0
#array_list = []
#rotate_length = 0


def rotate_array(array_list, array_length, rotate_length):
    output_array = []
    for j in range(rotate_length, array_length):
        output_array.append(array_list[j])
    for k in range(0, rotate_length):
        output_array.append(array_list[k])
    print(*output_array)
    return


for i in range(test_cases):
    input_two = input()
    input_split = input_two.split(" ")
    array_length = int(input_split[0])
    rotate_length = int(input_split[1])
    array_input = input()
    array_list = array_input.split(" ")
   # rotate_length = int(input())
    rotate_array(array_list, array_length, rotate_length)

# second solution
t = int(input())

while(t > 0):
    n = int(input())
    arr = list(map(int, (input().split())))
    d = int(input())
    brr = [0]*(n)
    for i in range(0, n):
        k = n-d+i
        if (k >= n):
            k = k-n
        brr[k] = arr[i]
    for i in range(n):
        print(brr[i], end=" ")
    print()

    t -= 1

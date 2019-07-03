def check_odd_pos(l_bin, count_l_bin):
    flag1 = False
    for i in range(1, count_l_bin, 2):
        if(l_bin[i] == "0"):
            falg1 = True
        else:
            return False
    return True


def find_bin(next_even):
    bin = f"{next_even:b}"
    s_bin = str(bin)
    l_bin = list(s_bin)
    count_l_bin = len(l_bin)
    flag = check_odd_pos(l_bin, count_l_bin)
    if(flag):
        return flag


def find_replacement(input_arr_num):
    if(input_arr_num % 2 == 0):
        next_even = input_arr_num + 2
    else:
        next_even = input_arr_num + 1

    status = find_bin(next_even)
    if(status):
        return next_even

    else:
        return find_replacement(next_even)


def check_neg(input_arr_int):
    pre_num = 0
    index = 0
    for i in input_arr_int:
        if(i == -1):
            result = find_replacement(pre_num)
            input_arr_int[index] = result
        pre_num = i
        index += 1


test_case = int(input())

for i in range(test_case):
    input_data = input()
    input_arr = input_data.split(" ")
    input_arr_int = list(map(int, input_arr))
    check_neg(input_arr_int)
    total = sum(input_arr_int)
    print(total)

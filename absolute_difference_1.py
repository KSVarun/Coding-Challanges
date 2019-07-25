# Given an array A of size N. Print all the numbers less than K in the array. The numbers should be such that the difference between every adjacent digit should be 1.

# Note: Print '-1' if no number if valid.

# Input:
# The first line consists of an integer T i.e number of test cases. T testcases follow. Each testcase contains two lines of input. The first line consists of two integers N and K separated by a space. The next line consists of N spaced integers.

# Output:
# For each testcase, print the required output.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= K, A[i] <= 1018

# Example:
# Input:
# 2
# 8 54
# 7 98 56 43 45 23 12 8
# 10 1000
# 87 89 45 235 465 765 123 987 499 655

# Output:
# 43 45 23 12
# 87 89 45 765 123 987

# Explanation:
# Testcase1: 43 45 23 12  all these numbers have adjacent digits diff as 1 and they are less than 54


def current_number_with_abs_diff_1(number):

    if number < 10:
        return False
    number = str(number)

    for i in range(len(number)-1):
        diff = abs(int(number[i]) - int(number[i+1]))
        if diff != 1:
            return False
    return True


def absolute_difference_of_1(array, k):
    result = list()

    for ele in array:
        if ele < k and current_number_with_abs_diff_1(ele):
            result.append(ele)

    if not result:
        result = [-1]

    return result


t = int(input())
for i in range(t):
    n, k = input().split()
    n, k = int(n), int(k)
    array = [int(_) for _ in input().split()]
    print(*absolute_difference_of_1(array, k))


# 2nd sol


t = int(input())

while t:
    t -= 1

    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))

    tmp = []
    for i in arr:
        if i < k:
            tmp.append(i)

    vv = False
    for i in tmp:
        ll = list(map(int, str(i)))
        l = len(ll)
        v = True
        for j in range(l-1):
            if abs(ll[j] - ll[j+1]) != 1:
                v = False
                break
        if v and l > 1:
            vv = True
            print(i, end=" ")

    if vv:
        print()
    else:
        print("-1")

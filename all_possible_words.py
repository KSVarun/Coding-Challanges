# code
# Given a keypad as shown in diagram, and an N digit number. List all words which are possible by pressing these numbers.


# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line of each test case is N, N is the number of digits. The second line of each test case contains D[i], N number of digits.

# Output:
# Print all possible words from phone digits with single space in lower case.

# Constraints:
# 1 <= T <= 10
# 1 <= N <= 10
# 2 <=  D[i] <= 9

# Example:
# Input:
# 1
# 3
# 2 3 4

# Output:
# adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi

# words = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
#          6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}


def possible_words(array):

    all_possible_words = [ele for ele in words.get(array[0])]

    for number in array[1:]:
        new_words = list()
        word = words.get(number)
        for i in range(len(all_possible_words)):
            for alphabet in word:
                new_words.append(all_possible_words[i] + alphabet)
        all_possible_words = new_words
        # print(new_words)

    return(all_possible_words)


t = int(input())
for i in range(t):
    n = int(input())
    array = [int(_) for _ in input().split()]
    print(*possible_words(array))

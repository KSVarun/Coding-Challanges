# Given a string s, remove all consonants and prints the string s that contains vowels only.
# Input: The first line of input contains integer T denoting the number of test cases. For each test case, we input a string.
# Output: For each test case, we get a string containing only vowels. If the string doesn't contain any vowels, then print "No Vowel"

# Constraints:

# 1<=T<=100

# The string should consist of only alphabets.

# Examples:

# Input: geEks
# Output: eE
# Input: what are you doing
# Output: a ae ou oi


def removecons(st):
    vowels = ["a", "i", "u", "o", "e"]
    for x in st:
        if x.lower() not in vowels and x != " ":
            st = st.replace(x, "")
    if st:
        return(st)
    else:
        return("No Vowel")


for _ in range(int(input())):
    st = input()
    print(removecons(st))

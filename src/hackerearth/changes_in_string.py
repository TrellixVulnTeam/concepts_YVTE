'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

'''
"""
4
3
AAB
5
AABAA
1
B
4
BABA

"""


# Write your code here

def solve_recur(index, str_in, cum_a):
    if index >= len(str_in):
        return 0
    else:
        index_a = index + 1
        while index_a < len(str_in) and str_in[index_a] == 'A':
            index_a += 1

        return min(cum_a[index], 1 + solve_recur(index_a, str_in, cum_a))


def solve_iter(str_in, cum_a):
    ans = [0 for i in range(len(str_in))]
    j = len(str_in) - 2
    # it does not matter whether last char is B or A... it's cost will be zero
    # our ans will be solved finally in index 0
    while j >= 0:
        if str_in[j] == 'A':
            ans[j] = ans[j + 1]
        else:
            ans[j] = min(cum_a[j], 1 + ans[j + 1])

        j -= 1

    return ans[0]


num_t = int(input())
for t in range(num_t):
    _ = input()
    str_in = input()

    len_s = len(str_in)
    count = 0

    cum_a = [0 for x in range(len_s)]
    index = len_s - 2

    while index >= 0:
        if str_in[index + 1] == 'A':
            cum_a[index] = cum_a[index + 1] + 1
        else:
            cum_a[index] = cum_a[index + 1]
        index -= 1

    # print(cum_a)

    index_a = 0
    if str_in[index_a] == 'A':
        while index_a < len(str_in) and str_in[index_a] == 'A':
            index_a += 1
        # count = solve_recur(index_a, str_in, cum_a)
        count_iter = solve_iter(str_in, cum_a)
    else:
        # count = solve_recur(0, str_in, cum_a)
        count_iter = solve_iter(str_in, cum_a)

    print(count_iter)



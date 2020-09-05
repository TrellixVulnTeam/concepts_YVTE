"""
Sorting Algorithms
"""


def bubble_sort(some_list, use_done=False, ascending=True):
    """
    Basic sorting
    :param some_list:
    :param use_done:
    :return:
    """
    list_ans = some_list.copy()
    len_list = len(list_ans)

    # i takes care of N passes of the array
    for i in range(len_list):
        # Each pass we'll assume the array may be sorted
        done = True
        print(f"before pass {i}: {list_ans}")

        for j in range(1, len_list):
            # Compare and swap if necessary
            if ascending:
                if list_ans[j - 1] > list_ans[j]:
                    list_ans[j - 1], list_ans[j] = list_ans[j], list_ans[j - 1]

                    # To track if we made any comparison
                    done = False
            else:
                if list_ans[j - 1] < list_ans[j]:
                    list_ans[j - 1], list_ans[j] = list_ans[j], list_ans[j - 1]

                    # To track if we made any comparison
                    done = False

        print(f"after pass {i}: {list_ans}")
        if use_done:
            if done:
                # The array is sorted and stop
                break
    return list_ans


def call_bubble():
    list_a = [2, 10, 45, 23, 5, 7, 39, 58, 60]
    list_ans = bubble_sort(list_a, False)
    print(f"unsorted: {list_a} and sorted: {list_ans}")

    print(f"{''.join(['-' * 100])}")
    list_ans = bubble_sort(list_a, True)
    print(f"unsorted: {list_a} and sorted: {list_ans}")

    print(f"{''.join(['-' * 100])}")
    list_ans = bubble_sort(list_a, True, False)
    print(f"Descending: unsorted: {list_a} and sorted: {list_ans}")


def merge_two_lists(list_a, list_b):
    # Assumption is that list_a and list_b are individually sorted.
    list_final = []
    ptr_a = 0
    ptr_b = 0
    len_list_a = len(list_a)
    len_list_b = len(list_b)

    while ptr_a < len_list_a and ptr_b < len_list_b:
        if list_a[ptr_a] <= list_b[ptr_b]:
            list_final.append(list_a[ptr_a])
            ptr_a += 1
        else:
            list_final.append(list_b[ptr_b])
            ptr_b += 1

    if ptr_a < len_list_a:
        list_final += list_a[ptr_a:]

    elif ptr_b < len_list_b:
        list_final += list_b[ptr_b:]

    return list_final


def merge_sort(list_x):
    if len(list_x) < 2:
        return list_x

    mid = len(list_x) // 2

    list_a = list_x[:mid]
    list_b = list_x[mid:]

    list_a = merge_sort(list_a)
    list_b = merge_sort(list_b)

    list_ans = merge_two_lists(list_a, list_b)

    return list_ans


def call_merge():
    # Merging example
    list_a = [7, 10, 23, 58]
    list_b = [2, 5, 39, 60, 100]

    list_ans = merge_two_lists(list_a, list_b)
    print(f"list_a: {list_a}\nlist_b: {list_b}\nmerged: {list_ans}")

    print(f"{''.join(['-' * 100])}")

    # Merge sort example
    list_x = [3, 9, 34, 99, 78, 23, 88, 101]
    print(f"list_x: {list_x}")
    list_ans = merge_sort(list_x.copy())
    print(f"sorted: {list_ans}")


def main():
    # call_bubble()
    call_merge()


if __name__ == '__main__':
    main()

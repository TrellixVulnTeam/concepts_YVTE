"""
Efficient code to calculate maximum subarray sum
Complexity: O(n)
Solution's name: Kadane's Algorithm
"""


def max_subarray_sum(list_nums: list) -> int:
    """
    The crux of the algorithm is to think of a sub-problem:
    We assume that we can select no subset and then the maximum sum = 0
    To calculate maximum possible subarray sum at position k, take optimal decision at position k:
    1. Exclude k: then maximum sum is only val at k
    2. Include k: Add past sum at k-1 and val at k
    This way it is necessary and enough to say that every k-1 max_sum is also the optimal max_sum
    @param list_nums:
    @return:
    """
    max_sum = 0
    temp_sum = 0
    for pos, val in enumerate(list_nums):
        temp_sum = max(val, temp_sum + val)
        max_sum = max(max_sum, temp_sum)

    return max_sum


def main():
    list_nums = [-1, 2, 4, -3, 5, 2, -5, 2]  # Expected answer = 10

    ans = max_subarray_sum(list_nums)
    assert ans == 10


if __name__ == '__main__':
    main()

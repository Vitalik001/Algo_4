import doctest
from typing import List


def solve(arr: List[int]) -> int:
    """
    :param arr:
    :return:
    >>> solve([2,3,4,2])
    1
    >>> solve([1,2,3,4])
    2
    >>> solve([1,2,3,4,5,6,7,8,9,10])
    5
    >>> solve([5,5,5,5,5,5,3])
    1
    >>> solve([1])
    1
    """
    sorted_arr=merge_sort(arr)
    occurrence_distribution=[]
    number_of_elements=1;
    for idx in range(1, len(arr)):
        if sorted_arr[idx]!=sorted_arr[idx-1]:
            occurrence_distribution.append(number_of_elements)
            number_of_elements=1
            continue
        number_of_elements += 1
        continue
    occurrence_distribution.append(number_of_elements)
    occurrence_distribution=merge_sort(occurrence_distribution)
    result=0
    original_length=length=len(arr)
    while length>original_length/2:
        length-=occurrence_distribution[-1]
        occurrence_distribution.pop()
        result+=1
    return result






def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

if __name__ == "__main__":
    print(doctest.testmod())


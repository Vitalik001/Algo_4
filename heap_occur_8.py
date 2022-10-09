def left(i):
    """
    Returns left child of A[i] in Heap
    :param i: index of parent
    :return: index of elem in A
    """
    return 2 * i


def right(i):
    """
    Returns right child of A[i] in Heap
    :param i: index of parent
    :return: index of elem in A
    """
    return 2 * i + 1


def BuildMaxHeap(A):
    """
    Builds MaxHeap from an array
    :param A: list
    :return: None
    >>> lst = [1, 2, 3, 4, 5, 6]
    >>> BuildMaxHeap(lst)
    >>> lst
    [6, 5, 3, 4, 2, 1]
    >>> lst = [1, 5, 3, 2, 8, 7]
    >>> BuildMaxHeap(lst)
    >>> lst
    [8, 7, 5, 2, 3, 1]
    >>> lst = [12, 7, 3, 2, 1, 9, 15, 14, 13, 24, 23, 17, 10]
    >>> BuildMaxHeap(lst)
    >>> lst
    [24, 23, 17, 15, 13, 12, 10, 14, 3, 1, 9, 7, 2]
    """
    i = len(A) // 2
    while i > 0:
        i -= 1
        BubbleDown(A, i)


def BubbleDown(A, i):
    """
    Heap A, index i
    BubbleDown for Heap
    :return: None
    >>> lst = [8, 7, 5, 2, 4, 3]
    >>> lst[0] = 1
    >>> BubbleDown(lst, 0)
    >>> lst
    [7, 5, 4, 2, 1, 3]
    >>> lst[1] = 0
    >>> BubbleDown(lst, 1)
    >>> lst
    [7, 4, 3, 2, 1, 0]
    """
    while True:
        p = left(i)
        q = p + 1
        largest = i
        if satisfies(p, A) and A[p] > A[largest]:
            largest = p
        if satisfies(q, A) and A[q] > A[largest]:
            largest = q
        if largest == i:
            return
        else:
            A[i], A[largest] = A[largest], A[i]
            i = largest


def satisfies(ind, array: list) -> bool:
    """
    Checks if ind < len(array)
    :param ind: index
    :param array: list
    :return: bool
    """
    return -1 < ind < len(array)


class Solution:
    @staticmethod
    def solve(array: list[int]) -> int:
        """
        Takes an array of integers, returns by some strange rules a number that's left
        :param array:
        :return: result
        >>> lst = [13, 53, 45, 3, 5, 0, -3, 45, 6, 7, 89, 69, 37, 420, 55]
        >>> Solution.solve(lst)
        4
        >>> lst = [1]
        >>> Solution.solve(lst)
        1
        >>> lst = [2,7,4,1,8,1]
        >>> Solution.solve(lst)
        1
        >>> lst = [12, 7, 3, 2, 1, 9, 15, 14, 13, 24, 23, 17, 10]
        >>> Solution.solve(lst)
        0
        """
        BuildMaxHeap(array)
        while len(array) > 2:
            y = 0
            if array[1] >= array[2]:
                x = 1
            else:
                x = 2
            if array[y] == array[x]:
                first = array.pop()
                second = array.pop()
                array[y] = first
                if len(array) > 2:
                    array[x] = second
            else:
                leaf = array.pop()
                array[y] -= array[x]
                array[x] = leaf
            BubbleDown(array, x)
            BubbleDown(array, y)
        if len(array) == 1:
            return array[0]
        return 0 if array[0] == array[1] else array[0] - array[1]

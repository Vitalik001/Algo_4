import doctest
from typing import List


def solve(nums: List[int], k: int) -> List[int]:
    """
    :param nums:
    :param k:
    :return:
    >>> solve([1,3,-1,-3,5,3,6,7],3)
    [3, 3, 5, 5, 6, 7]
    >>> solve([4,-2],2)
    [4]
    >>> solve([1, 10, 20, 4, 47, -3, -1, -7], 2)
    [10, 20, 20, 47, 47, -1, -1]
    >>> solve([1, 10, 20, 4, 47, -3, -1, -7], 3)
    [20, 20, 47, 47, 47, -1]
    """
    result=[]
    heap=[(el, idx) for idx, el in enumerate(nums[:k])]
    build_max_heap(heap)
    result.append(heap[0][0])
    for last_idx in range(k, len(nums)):
        new_element=(nums[last_idx], last_idx)
        heap.append(new_element)
        # print(heap)
        bubble_up(heap, len(heap)-1)
        # print(heap)
        while heap[0][1]<=last_idx-k:
            extract_first(heap)
            # print(heap, 'while')
        result.append(heap[0][0])
    return result


def find_parent(x):
    return x//2

def left(x):
    return 2*x+1

def right(x):
    return 2*x+2

def extract_first(arr):
    arr[0], arr[-1]=arr[-1], arr[0]
    arr.pop()
    max_heapify(arr, 0)

def bubble_up(arr, idx):
    p=find_parent(idx)
    if arr[p][0]<arr[idx][0]:
        arr[p], arr[idx]=arr[idx], arr[p]
        bubble_up(arr, p)

def max_heapify(arr, x):
    l=left(x)
    r=right(x)
    if l<len(arr) and arr[l][0]>arr[x][0]:
        largest = l
    else:
        largest = x
    if r<len(arr) and arr[r][0]>arr[largest][0]:
        largest=r
    if largest!=x:
        arr[x], arr[largest]=arr[largest], arr[x]
        max_heapify(arr, largest)

def build_max_heap(arr):
    for i in range(len(arr)//2+1, -1, -1):
        max_heapify(arr, i)


if __name__ == "__main__":
    print(doctest.testmod())

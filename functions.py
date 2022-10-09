from typing import List
def left(i: int):
    return  2*i
def right(i: int):
    return 2*i+1

def max_heapify(A: List[int], i:int):
    p = left(i)
    q = right(i)
    largest = i
    if p <= len(A) and A[p-1] > A[i-1]:
        largest = p
    if q <= len(A) and A[q-1] > A[i-1]:
        largest = q
        if p <= len(A) and A[q - 1] < A[p-1]:
            largest = p
    if largest == i:
        return
    # print(A[i-1], A[largest-1])
    A[i-1], A[largest-1] = A[largest-1], A[i-1]
    # print(A)
    max_heapify(A, largest)

def max_heap(A:List[int]):
    for i in range(len(A) // 2, 0, -1):
        max_heapify(A, i)

def extract_max(A:List[int]):
    max = A[0]
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    A.pop()
    max_heapify(A, 1)
    return max

def insert(A:List[int], val:int):
    A.insert(0, val)
    max_heapify(A, 1)
import doctest
from typing import List
from functions import *

# Вам дано масив B що містить n додатних чисел. З початкового масиву А, що
# містить n чисел 1, ви можете виконувати наступну операцію:
# ● Нехай x - сума всіх елементів в масиві А
# ● Виберіть індех i такий що 0 <= i < n та встановіть значення А[i] рівне x.
# ● Ви можете виконувати дану процедуру довільну кількість раз.
# Функція повинна повертати true, якщо можливо отримати масив B з початкового
# масиву А за допомогою використання описаної операції 0 або більше разів. В іншому
# випадку поверніть false. Час виконання O(n logn)

def solve(A: List[int]) -> bool:
    """
    >>> solve([9, 5, 3])
    True
    >>> solve([1, 1, 1, 2])
    False
    >>> solve([])
    
    >>> solve([1])
    True
    >>> solve([9])
    False
    """
    total = sum(A)
    if len(A)==0:
        return None
    if len(A) == 1:
        if A[0] == 1:
            return True
        else:
            return False
    max_heap(A)
   
    while A[0]>1:
        max = A[0]
        if max <= total - max: #тому що перед тим там мало бути ще хоча б число 1
            return False
        extract_max(A)
        insert(A, max%(total-max))   
        total = total - max + max%(total-max)        
    return True
# print(solve([9]))
# doctest.testmod()
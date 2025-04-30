import random

def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k повинно бути в межах довжини масиву")

    def select(lst, k):
        pivot = random.choice(lst)
        lows = [el for el in lst if el < pivot]
        highs = [el for el in lst if el > pivot]
        pivots = [el for el in lst if el == pivot]

        if k <= len(lows):
            return select(lows, k)
        elif k <= len(lows) + len(pivots):
            return pivots[0]
        else:
            return select(highs, k - len(lows) - len(pivots))

    return select(arr, k)

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}-й найменший елемент: {quick_select(arr, k)}")

def find_min_max(arr):
    def helper(low, high):
        # Якщо один елемент
        if low == high:
            return arr[low], arr[low]

        # Якщо два елементи
        elif high == low + 1:
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]

        # Інакше - розділяй і володарюй
        else:
            mid = (low + high) // 2
            min1, max1 = helper(low, mid)
            min2, max2 = helper(mid + 1, high)
            return min(min1, min2), max(max1, max2)

    if not arr:
        raise ValueError("Масив не може бути порожнім")
    return helper(0, len(arr) - 1)


arr = [3, 1, 5, 2, 8, 4]
result = find_min_max(arr)
print(f"Мінімум: {result[0]}, Максимум: {result[1]}")

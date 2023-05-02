def sumNumbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)


def f(x):
    if x == 1:
        return 'Even'
    elif x == 2.3:
        return 23
    return


def newString(symbol, count=3):  # значение count задано по умолчанию
    return symbol * count


def concatenatio(*params):  # * позволяет передавать неограниченное кол-во аргументов
    # и работает только со строковым значением
    res = ""
    for item in params:
        res += item
    return res


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1)+fib(n-2)


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def mergeSort(nums):  # сортировка слиянием
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

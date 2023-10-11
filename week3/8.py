import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sub_arrays = [[x] for x in arr]

    while len(sub_arrays) > 1:
        new_sub_arrays = []
        for i in range(0, len(sub_arrays), 2):
            if i + 1 < len(sub_arrays):
                merged = merge(sub_arrays[i], sub_arrays[i + 1])
            else:
                merged = sub_arrays[i]
            new_sub_arrays.append(merged)
        sub_arrays = new_sub_arrays

    return sub_arrays[0]
def generate_random_list(length):
    return [random.randint(1, 1000) for _ in range(length)]


# 不同长度的数列
list_lengths = [1000, 10000, 30000]

for length in list_lengths:
    random_list = generate_random_list(length)

    # 使用选择排序并计时
    selection_copy = random_list.copy()
    start_time = time.time()
    selection_sort(selection_copy)
    end_time = time.time()
    selection_sort_time = end_time - start_time

    # 重新生成随机数列
    random_list = generate_random_list(length)

    # 使用归并排序并计时
    merge_copy = random_list.copy()
    start_time = time.time()
    merge_sort(merge_copy)
    end_time = time.time()
    merge_sort_time = end_time - start_time

    print(f"List length: {length}")
    print(f"Selection Sort Time: {selection_sort_time} seconds")
    print(f"Merge Sort Time: {merge_sort_time} seconds")



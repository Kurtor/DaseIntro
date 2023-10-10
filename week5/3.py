def insertion_sort(data):
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and data[j] > current:
            data[j + 1] = data[j]
            j -= 1
            data[j + 1] = current


data = [1, 19, 5, 7, 6, 8, 10, 6, 3]
insertion_sort(data)
print(data)

"""Question 2: Randomized Quicksort."""
import random


def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot - 1)
        randomized_quicksort(arr, pivot + 1, high)


if __name__ == "__main__":
    values = [45, 12, 78, 23, 9, 56, 31]
    print("Original array:", values)
    randomized_quicksort(values, 0, len(values) - 1)
    print("Sorted array:", values)

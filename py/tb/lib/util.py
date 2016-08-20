import random

def shuffle(cards):
    max = len(cards)-1
    while max != 0:
        r = random.randint(0, max)
        cards[r], cards[max] = cards[max], cards[r]
        max = max - 1
    return cards

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def qsort(arr, left, right):
    if left >= right:
        return
    swap(arr, left, (left + right) // 2)

    last = left
    i = left + 1
    while i <= right:
        if arr[i] > arr[left]:
            last += 1
            swap(arr, last, i)
        i += 1
    swap(arr, last, left)
    qsort(arr, left, last - 1)
    qsort(arr, last + 1, right)
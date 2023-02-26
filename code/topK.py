import random


def sift(array, low, high):
    i = low
    j = 2 * i + 1
    heap = array[i]
    while j <= high:
        if j + 1 <= high and array[j + 1] < array[j]:
            j = j + 1

        if array[j] < heap:
            array[i] = array[j]
            i = j
            j = 2 * i + 1
        else:
            array[i] = heap
            break
    else:
        array[i] = heap


def top_k(array, k):
    # 1. 创建一个k大小的列表
    heap = array[:k]
    # 2. 使其成为小根堆
    for i in range((k - 1 - 1) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 3. 判断 其余元素是否比小根堆的根还大
    # for item in heap[k:]:
    for item in li[k:]:
        if item > heap[0]:
            heap[0] = item
            sift(heap, 0, k - 1)
    # 4.对小根堆排序
    for i in range(k - 1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        sift(heap, 0, i - 1)  # high前移
    return heap


li = list(range(1000))

random.shuffle(li)
print(li)
print(top_k(li, 10))

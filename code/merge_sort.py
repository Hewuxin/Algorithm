import random


def merge(array, low, mid, high):

    i = low  # 左边有序列表第一个数的下标
    j = mid + 1  # 右边有序列表第一个数的下标
    tmp = list()
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    # wrong
    # if i <= mid:
    #     tmp.extend(array[i:mid])
    # if j <= high:
    #     tmp.extend(array[j:high + 1])
    # right 1
    if i > mid:  # 表示 low～mid 的元素全部取完
        tmp.extend(array[j:high + 1])
    if j > high:  # 表示 mid～high的元素全部取完
        tmp.extend(array[i:mid + 1])
    # right 2
    # array[low:high + 1] = tmp
    # while i <= mid:
    #     tmp.append(array[i])
    #     i += 1
    # while j <= high:
    #     tmp.append(array[j])
    #     j += 1
    array[low:high + 1] = tmp


def merge_sort(array, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, high)
        merge(array, low, mid, high)


li = list(range(100))

random.shuffle(li)
print(li)
merge_sort(li, 0, len(li) - 1)
print(li)

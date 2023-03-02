import random


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # 插入排序
        tmp = li[i]  # tmp代表新到的数
        j = i - gap  # j 是已经排好序的最后一个元素的下表
        while j >= 0 and tmp < li[j]:  # 在 j遍历完已经排好序或者 tmp大于当前元素时跳出循环
            li[j + gap] = li[j]  # 将当前元素后移一个位置
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    gap = len(li) // 2

    while gap >= 1:
        insert_sort_gap(li, gap)
        gap = gap // 2


def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and tmp < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


array = list(range(100))
random.shuffle(array)
print(array)
shell_sort(array)
print(array)

array1 = list(range(100))
random.shuffle(array1)
print(array1)
insert_sort(array1)
print(array1)

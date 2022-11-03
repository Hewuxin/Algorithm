import random


def bubble_sort_v1(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort_v2(array):
    # 利用 布尔值作为标记
    for i in range(len(array) - 1):
        is_sorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
        if is_sorted:
            break


def bubble_sort_v3(array: []):
    # 记录最后一次交换的位置
    last_exchange_index = 0
    # 无序数列的边界，每次比较只需要比到这里
    sort_border = len(array) - 1
    for i in range(len(array) - 1):
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                # 有元素交换，所以不是有序的，标记为False
                is_sorted = False
                # 把无序数列的边界更新为最后一次交换元素的位置
                last_exchange_index = j
        sort_border = last_exchange_index
        if is_sorted:
            break


def cock_tail_sort(array: []):
    """
    优点：能够在特定条件下，减少排序的回合数
    缺点：代码量几乎增加了1倍
    应用场景：大部分元素已经有序的情况下
    :param array:
    :return:
    """
    for i in range(len(array) // 2):
        is_sorted = True
        # 奇数轮，从左向右比较和交换
        for j in range(i, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
        if is_sorted:
            break
        # 偶数轮之前，重新标记为True
        is_sorted = True
        for j in range(len(array) - i - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                is_sorted = False
        if is_sorted:
            break


def bubble_sort_review(array: []):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort_review01(array: []):
    """
    改进版 冒泡排序
    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        exchange = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                exchange = True
        if not exchange:
            return


if __name__ == '__main__':
    data_list = [3, 4, 2, 1, 5, 6, 7, 8]
    # data_list = [2, 3, 4, 5, 6, 7, 8, 1]
    # data_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    # cock_tail_sort(data_array)
    # print(data_array)
    # random_array = [random.randint(1, 100) for _ in range(10)]
    # print(random_array)
    print(data_list)
    bubble_sort_review01(data_list)
    print(data_list)
    #
    # bubble_sort_review01(data_list)

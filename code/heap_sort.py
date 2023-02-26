import random


def sift(array, low, high):
    """

    :param array:
    :param low:  堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    tmp = array[low]
    i = low  # 刚开始指向根的位置
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and array[j + 1] > array[j]:  # 如果右子节点存在且大于左子节点
            j = j + 1

        if array[j] > tmp:
            array[i] = array[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:
            array[i] = tmp  # tmp作为某一个子堆的父节点
            break
    else:
        array[i] = tmp  # tmp只能作为最底层子节点存在


def heap_sort(array):
    n = len(array)
    # 1.建堆  从最后一个子节点所在的子堆开始向下调整
    for i in range((n - 1 - 1) // 2, -1, -1):
        sift(array, i, n - 1)

    # 2.排序
    for i in range(n - 1, -1, -1):
        array[i], array[0] = array[0], array[i]  # 将当前大根堆的根放到数组最后
        # sift(array, i - 1, n - 1)  # 进行一次向下调整
        sift(array, 0, i - 1)  # 是当前堆重新成为大根堆


li = list(range(100))

random.shuffle(li)
print(li)
heap_sort(li)
print(li)

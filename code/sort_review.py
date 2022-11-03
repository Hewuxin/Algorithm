def bubble_sort(li):
    for i in range(len(li) - 1):  # 冒泡的轮次
        for j in range(len(li) - i - 1):  # 冒泡的过程
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def select_sort(li):
    for i in range(len(li) - 1):  # 当前选择的数
        min_loc = i
        for j in range(i + 1, len(li)):  # 从无序区找出最小的数的下标
            if li[j] < li[min_loc]:
                min_loc = j
        li[min_loc], li[i] = li[i], li[min_loc]


def insert_sort(li):
    for i in range(1, len(li)):  # 摸到的牌
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:  # 从手牌中找出合适的位置
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


def partition(li, left, right):
    tmp = li[left]

    while left < right:
        while left < right and li[right] >= tmp:  # 从右面找比tmp小的数
            right -= 1   # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边

        while left < right and li[left] <= tmp:  # 从左边找比tmp大的数
            left += 1
        li[right] = li[left]  # 将比tmp大的数写到右边
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


if __name__ == '__main__':
    data_list = [3, 4, 2, 1, 5, 6, 7, 8]
    print(data_list)
    # bubble_sort(data_list)
    # select_sort(data_list)
    # insert_sort(data_list)
    quick_sort(data_list, 0, len(data_list) - 1)
    print(data_list)

# def partition(li, left, right):
#     temp = li[left]
#     while left < right:
#         while left < right and li[right] >= temp:  # 从右面找比tmp小的数
#             right -= 1   # 往左走一步
#         li[left] = li[right]  # 把右边的值写到左边
#
#         while left < right and li[left] <= temp:   # 从左边找比temp大的数
#             left += 1
#         li[right] = li[left]
#     li[left] = temp
#     return left
#
#
# def quick_sort(li, left, right):
#     if left < right:
#         mid = partition(li, left, right)
#         quick_sort(li, left, mid - 1)
#         quick_sort(li, mid + 1, right)


def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]

    li[left] = temp
    return left


def quick_sort_review(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort_review(li, left, mid - 1)
        quick_sort_review(li, mid + 1, right)


if __name__ == '__main__':
    data_list = [3, 4, 2, 1, 5, 6, 7, 8]
    print(data_list)
    quick_sort_review(data_list, 0, len(data_list) - 1)
    print(data_list)

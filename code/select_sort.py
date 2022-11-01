def select_sort(array: []):
    """

    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        tmp = array[i]
        min_loc = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_loc]:
                min_loc = j
        array[i], array[min_loc] = array[min_loc], array[i]


if __name__ == '__main__':
    data_list = [3, 4, 2, 1, 5, 6, 7, 8]
    print(data_list)
    select_sort(data_list)
    print(data_list)
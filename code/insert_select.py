def insert_select(array: []):
    for i in range(1, len(array)):  # 摸到牌的下标
        j = i - 1  #
        tmp = array[i]
        while j >= 0 and array[j] > tmp:  # 遍历手牌 寻找合适位置
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = tmp  # 插入摸到的牌


if __name__ == '__main__':
    data_list = [3, 4, 2, 1, 5, 6, 7, 8]
    print(data_list)
    insert_select(data_list)
    print(data_list)
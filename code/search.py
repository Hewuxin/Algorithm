def func1(x):
    """
    会无限循环下去
    :param x: int
    :return:
    """
    print(x)
    func1(x - 1)


def func2(x):
    """
    会无限循环下去
    :param x:
    :return:
    """
    if x > 0:
        print(x)
        func2(x + 1)


def func3(x):
    """
        输入X为5 输出结果为5 4 3 2 1
    :param x:
    :return:
    """
    if x > 0:
        print(x)
        func3(x - 1)


def func4(x):
    """
    输入X为5 输出结果为1 2 3 4 5
    :param x:
    :return:
    """
    if x > 0:
        func4(x - 1)
        print(x)


def haoni(n, a, b, c):
    """
    汉诺塔问题
    n个盘子时：
     > 1.把n-1个圆盘从A经过C移动到B
     > 2.把第n个圆盘从A移动到C
     > 3.把n-1个小圆盘从B经过A移动到C
    """
    if n > 0:
        haoni(n - 1, a, c, b)
        print(n, " moving from %s to %s" % (a, c))
        haoni(n - 1, b, a, c)


def linear_search(data_list, target_value):
    """
    线性查找
    :param data_list:
    :param target_value:
    :return:
    """
    for i, val in enumerate(data_list):
        if val == target_value:
            return i
    else:
        return None


def binary_search(data_list, target_value):
    left = 0
    right = len(data_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if data_list[mid] == target_value:
            return mid
        elif data_list[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return None


if __name__ == '__main__':
    # func3(5)
    # func4(5)
    # haoni(3, "A", "B", "C")
    data_list = list(range(100))
    print(linear_search(data_list, 50))
    print(binary_search(data_list, 49))
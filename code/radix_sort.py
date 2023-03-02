import random


def radix_sort(li, max_num=10000):
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]  # 创建0~9十个桶
        for val in li:
            # 987
            # it = 0, 987 // 1 = 987 987 % 10 = 7
            # it = 1, 987 // 10 = 98 98 % 10 = 8
            # it = 2, 987 // 100 = 9 9 % 10 =9
            digit = (val // (10 ** it)) % 10
            buckets[digit].append(val)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1  # 依次对个 十 百 千 万。。。位分桶


array = [random.randint(0, 10000) for _ in range(1000)]
print(array)
radix_sort(array)
print(array)

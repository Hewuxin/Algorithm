import random


def bucket_sort(li, n=100, max_num=10000):
    # 创建桶
    buckets = [[] for _ in range(n)]
    for val in li:
        # 2101
        # max_num // n 代表每个桶的元素的个数
        # n-1 代表将max_num放到最后一个桶
        i = min(val // (max_num // n), n - 1)
        # 将元素放到它该去的桶
        buckets[i].append(val)
        # 接着给桶内元素排序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break

    sorted_li = list()
    for bucket in buckets:
        sorted_li.extend(bucket)


array = list(range(10000))
random.shuffle(array)
print(array)
bucket_sort(array)
print(array)

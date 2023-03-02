import random


def count_sort(li, max_num=100):
    count = [0 for _ in range(max_num + 1)]
    for val in li:
        count[val] += 1

    li.clear()
    for idx, val in enumerate(count):
        for _ in range(val):
            li.append(idx)


array = [random.randint(0, 100) for _ in range(50)]
print(array)
count_sort(array)
print(array)

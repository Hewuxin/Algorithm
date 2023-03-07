class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                # 保存当前节点
                cur_node = self.node
                # 指针后移
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)  # 创建节点
        if not self.head:  # 如果头节点指向为空，
            self.head = s
            self.tail = s
        else:
            self.tail.next = s  # 直接挂到最末尾，并将tail指针更新
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<" + ",".join(map(str, self)) + ">>"


class HashMap:
    def __init__(self, size=101):
        """
        hash map init
        :param size:
        """
        self.size = size
        # 创建size个槽用来存储value
        self.T = [LinkList() for _ in range(self.size)]

    def h(self, k):
        """
        hash function
        :param k:
        :return:
        """
        return k % self.size

    def insert(self, item):
        i = self.h(item)
        if self.find(item):
            print("Duplicated Insert.")
        else:
            self.T[i].append(item)

    def find(self, item):
        # 1. 根据哈希函数计算哈希值
        i = self.h(item)
        return self.T[i].find(item)


if __name__ == '__main__':
    ht = HashMap(7)
    ht.insert(1)
    ht.insert(3)
    ht.insert(8)
    ht.insert(10)
    ht.insert(5)
    ht.insert(7)
    for T in ht.T:
        print(str(T), end=" ")


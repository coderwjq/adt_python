# coding:utf-8

# 双向链表的相关操作：
# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历链表
# add(item) 链表头部添加
# append(item) 链表尾部添加
# insert(pos, item) 指定位置添加
# remove(item) 删除节点
# search(item) 查找节点是否存在


class Node(object):
    """节点"""

    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    """双向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head

        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next

        print("")

    def add(self, item):
        """链表头部添加，头插法"""
        node = Node(item)

        # 注意处理链表为空的情况
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
            node.next.prev = node

    def append(self, item):
        """链表尾部添加，尾插法"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head

            while cur.next is not None:
                cur = cur.next

            # cur当前指向最后一个节点
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加"""
        node = Node(item)

        # 头插法
        if pos <= 0:
            self.add(item)
        # 尾插法
        elif pos > (self.length() - 1):
            self.append(item)
        # 中间插入
        else:
            cur = self.__head
            count = 0

            while count < pos:
                count += 1
                cur = cur.next

            # 循环结束，cur指向要插入的位置
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        # 先考虑一般情况，再看一般情况下的代码是否适合特殊情况
        cur = self.__head

        while cur is not None:
            if cur.elem == item:
                # 判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    # 判断链表中是否只有一个节点
                    if cur.next is not None:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 判断是否是尾节点
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head

        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next

        return False


if __name__ == "__main__":
    dll = DoubleLinkedList()

    print("before initialized:", dll.is_empty())
    print("before initialized:", dll.length())

    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.add(4)
    dll.add(5)
    dll.add(6)
    dll.travel()

    dll.append(7)
    dll.travel()

    dll.insert(3, 100)
    dll.travel()

    dll.remove(3)
    dll.travel()

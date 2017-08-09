# coding:utf-8

# 单向循环链表的相关操作：
# is_empty() 判断链表是否为空
# length() 返回链表的长度
# travel() 遍历
# add(item) 在头部添加一个节点
# append(item) 在尾部添加一个节点
# insert(pos, item) 在指定位置pos添加节点
# remove(item) 删除一个节点
# search(item) 查找节点是否存在


class Node(object):
    """节点"""

    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleCycleLinkedList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node
        # 如果node不为空，则需要指向自己构成一个循环链表
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表的长度"""
        if self.is_empty():
            return 0
        else:
            cur = self.__head
            count = 1

            while cur.next is not self.__head:
                count += 1
                cur = cur.next

            return count

    def travel(self):
        """遍历"""
        if self.is_empty():
            return
        else:
            cur = self.__head

            while cur.next is not self.__head:
                print(cur.elem, end=" ")
                cur = cur.next

            # 循环结束，cur指向尾节点，但是尾节点元素尚未打印，需要单独输出
            print(cur.elem)

    def add(self, item):
        """在头部添加一个节点，头插法"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 需要获取到尾节点
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """在尾部添加一个节点，尾插法"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 同样需要获取到尾节点
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """在指定位置pos添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            prev = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                prev = prev.next
            # 循环结束，prev指向要插入位置的前一个元素
            node.next = prev.next
            prev.next = node

    def remove(self, item):
        """删除一个节点，需要考虑链表是否为空，删除的节点是头节点，尾节点，还是中间节点"""
        if self.is_empty():
            return
        else:
            cur = self.__head
            pre = None

            while cur.next is not self.__head:
                if cur.elem == item:
                    # 判断是头节点，还是中间节点
                    if cur is self.__head:
                        # 头节点，需要找到尾节点
                        rear = self.__head
                        while rear.next is not self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                    else:
                        # 中间节点
                        pre.next = cur.next

                    return
                else:
                    pre = cur
                    cur = cur.next

            # 退出循环，cur指向尾节点
            if cur.elem == item:
                # 注意判断链表中是否只有一个节点
                if cur is self.__head:
                    self.__head = None
                else:
                    pre.next = self.__head

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next is not self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            # 循环结束，cur指向尾节点，但是尾节点并未参与比较，需要单独进行判断的
            if cur.elem == item:
                return True
            else:
                return False


if __name__ == "__main__":
    scll = SingleCycleLinkedList()

    print("befor initialized:", scll.is_empty())
    print("befor initialized:", scll.length())

    scll.add(1)
    scll.add(2)
    scll.add(3)
    scll.add(4)
    scll.add(5)
    scll.add(6)
    scll.travel()

    scll.append(7)
    scll.travel()

    scll.insert(3, 99)
    scll.travel()

    print("scll.search(99):", scll.search(99))

    scll.remove(99)
    scll.travel()
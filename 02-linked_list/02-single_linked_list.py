# coding:utf-8

# 单链表的相关操作：
# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# search(item) 查找节点是否存在


class Node(object):
    """节点"""
    def __init__(self, elem):
        # 数据区
        self.elem = elem
        # 指向下一个节点
        self.next = None


class SingleLikedList(object):
    """单链表"""
    def __init__(self, node = None):
        # 头节点
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head

        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        # 创建一个Node
        node = Node(item)

        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        # 创建一个Node
        node = Node(item)

        # 如果链表为空
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head

            while cur.next != None:
                cur = cur.next

            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0

            # 1 2 3 4 5 6
            # pos = 3, item = 9
            while count < (pos - 1):
                count += 1
                pre = pre.next

            # 当循环结束后，pre指向要插入位置的前一个，即pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        pre = None
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next

        return False

if __name__ == "__main__":
    sll = SingleLikedList()
    print("initialized...")
    print("is_empty:", sll.is_empty())
    print("length:", sll.length())

    sll.append(1)
    print("is_empty:", sll.is_empty())
    print("length:", sll.length())
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.add(7)
    sll.travel()

    print("before insert exist -5:",sll.search(-5))
    sll.insert(-5, -5)
    print("after insert exist -5:", sll.search(-5))
    sll.travel()
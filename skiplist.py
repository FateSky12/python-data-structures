import random

class Node:
    def __init__(self, level, key, value):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.head = Node(self.max_level, None, None)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def insert(self, key, value):
        # 记录每层的前驱节点
        update = [None] * (self.max_level + 1)
        current = self.head

        # 从最高层开始查找
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # 到达最底层，指向下一个节点
        current = current.forward[0]

        # 如果当前节点的key等于要插入的key，则更新value
        if current and current.key == key:
            current.value = value
        else:
            # 随机生成一个层数
            rlevel = self.random_level()

            # 如果随机生成的层数大于当前最大层数，则更新update数组
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.head
                self.level = rlevel

            new_node = Node(rlevel, key, value)

            # 更新每层的指针
            for i in range(rlevel + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def delete(self, key):
        update = [None] * (self.max_level + 1) # 记录每层的前驱节点
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
        else:
            print(f"Key not found: {key}")

    def search(self, key):
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.key == key:
            print(f"Key: {key}, Value: {current.value}")
        else:
            print(f"Key not found: {key}")

    def display(self):
        print("\n***** Skip List *****")
        head = self.head
        for lvl in range(self.level + 1):
            print(f"Level {lvl}: ", end=" ")
            node = head.forward[lvl]
            while node:
                print(f"{node.key} -> ", end=" ")
                node = node.forward[lvl]
            print("")
        print("**********************")

def main():
    max_level = 3
    p = 0.5
    skip_list = SkipList(max_level, p)

    skip_list.insert(3, "A")
    skip_list.insert(6, "B")
    skip_list.insert(7, "C")
    skip_list.insert(9, "D")
    skip_list.insert(12, "E")
    skip_list.insert(19, "F")
    skip_list.insert(17, "G")
    skip_list.insert(26, "H")
    skip_list.insert(21, "I")
    skip_list.insert(25, "J")
    skip_list.insert(35, "K")
    skip_list.insert(40, "L")
    skip_list.insert(39, "M")
    skip_list.insert(50, "N")
    skip_list.insert(55, "O")
    skip_list.insert(60, "P")
    skip_list.insert(65, "Q")
    skip_list.insert(70, "R")
    skip_list.insert(80, "S")
    skip_list.insert(90, "T")
    skip_list.insert(100, "U")
    skip_list.display()

    skip_list.search(19)
    skip_list.search(29)

    skip_list.delete(19)
    skip_list.delete(29)
    skip_list.display()

if __name__ == "__main__":
    main()
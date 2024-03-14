class BIT:
    def __init__(self, n):
        self.n = n # 树状数组的长度
        self.tree = [0] * (n + 1) # 树状数组的下标从1开始，所以需要n+1个元素
        
    # 计算lowbit，即计算i的二进制表示中最右边的1所对应的值
    # E1: i=6，二进制表示为110，所以lowbit(6)=(10)_2=2
    # E2: i=7，二进制表示为111，所以lowbit(7)=(1)_2=1
    # E3: i=12，二进制表示为1100，所以lowbit(12)=(100)_2=4
    def lowbit(self, x):
        return x & (-x)
    
    def update(self, i, delta):
        print("更新第", i, "个元素，增加", delta)
        print("更新前树：", self.tree)
        while i <= self.n:
            self.tree[i] += delta
            i += self.lowbit(i) # 更新i的父节点
        print("现在的树：", self.tree)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res

# 初始化数组
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
bit = BIT(n)

# 将初始数组更新到树状数组
for i in range(n):
    bit.update(i+1, arr[i])

# 操作1: 将arr[1]增加3 (下标从1开始)
bit.update(2, 3)

# 操作2: 查询arr[1]到arr[5]的区间和
left = 1
right = 5
ans = bit.query(right) - bit.query(left-1)
print(ans)  # 输出 18

# 操作1: 将arr[4]增加6
bit.update(5, 6)

# 操作2: 查询arr[3]到arr[8]的区间和 
left = 3
right = 8
ans = bit.query(right) - bit.query(left-1)
print(ans) # 输出 39
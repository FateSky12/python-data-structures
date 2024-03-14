# 使用heapq模块实现最小堆
import heapq

a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(a)
print("heapify a:", a)

x = heapq.heappop(a)
print("heappop a:", x)

# 手写最小堆
class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def push(self, x):
        self.heap.append(x)
        self.size += 1
        self._swim(self.size)

    def pop(self):
        x = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._sink(1)
        return x

    def _swim(self, k):
        while k > 1 and self.heap[k] < self.heap[k//2]:
            self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def _sink(self, k):
        while 2*k <= self.size:
            j = 2*k
            if j < self.size and self.heap[j] > self.heap[j+1]:
                j += 1
            if self.heap[k] <= self.heap[j]:
                break
            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            k = j

# 使用手写最小堆
min_heap = MinHeap()
for i in a:
    min_heap.push(i)
print("min_heap:", min_heap.heap)

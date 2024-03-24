# 计算排列数和组合数
# 使用math库
import math

n, k = 5, 3
perm = math.perm(n, k)  # 排列数
comb = math.comb(n, k)  # 组合数
print(f'排列数：{perm}，组合数：{comb}')


# 使用阶乘计算全排列
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def permutation(n, k):
    return factorial(n) // factorial(n - k)


def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


perm = permutation(n, k)
comb = combination(n, k)

print(f"P({n}, {k}) = {perm}")
print(f"C({n}, {k}) = {comb}")


# 使用位掩码计算全排列
def permutations_bit(arr):
    def backtrack(path, mask):
        if len(path) == len(arr):
            result.append(path[:])  # 深拷贝，因为path会被修改
            return
        for i in range(len(arr)):
            if mask & (1 << i): continue  # 如果该位已被选中，则跳过
            backtrack(path + [arr[i]], mask | (1 << i))  # 选择当前元素并更新掩码

    result = []
    backtrack([], 0)
    return result

# 使用itertools库
from itertools import permutations, combinations

nums = [1, 2, 3]
perms = list(permutations(nums))
combs = list(combinations(nums, 2))
print(perms)
print(combs)

# 示例

print(permutations_bit(nums))

######################################################################
# reduce：对列表中的元素进行累加，如：[1, 2, 3, 4, 5] -> 1+2+3+4+5=15
from functools import reduce

# 计算列表中所有元素的和
result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(result)  # 输出: 15

######################################################################
# partial：用于部分应用一个函数，即固定函数的部分参数，返回一个新函数
from functools import partial

def multiply(x, y):
    return x * y

# 创建一个新函数，将multiply函数的第一个参数固定为2
double = partial(multiply, 2)
print(double(4))  # 输出: 8

######################################################################
# lru_cache：用于缓存函数的返回值，避免重复计算
from functools import lru_cache

@lru_cache(maxsize=32)
def get_pep(number):
    print(f"Fetching PEP {number}")
    return f"PEP {number} content"

print(get_pep(8))
print(get_pep(8))  # 第二次调用时，结果会从缓存中获取，不会打印"Fetching PEP 8"

######################################################################
# cmp_to_key：将比较函数转换为key函数，用于排序
from functools import cmp_to_key

def compare_items(x, y):
    return x - y

sorted_list = sorted([5, 2, 4, 1, 3], key=cmp_to_key(compare_items))
print(sorted_list)  # 输出: [1, 2, 3, 4, 5]

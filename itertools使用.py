######################################################################
# pairwise：两两组合，如[1, 2, 3, 4, 5] -> (1, 2), (2, 3), (3, 4), (4, 5)
from itertools import pairwise

lst = [1, 2, 3, 4, 5]
# 使用pairwise进行两两迭代
for a, b in pairwise(lst):
    print(f'{a} + {b} = {a+b}')

######################################################################
# chain：将多个可迭代对象连接起来，如[1, 2, 3]和[4, 5, 6] -> [1, 2, 3, 4, 5, 6]
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(chain(list1, list2))
print(combined)  # 输出: [1, 2, 3, 4, 5, 6]

######################################################################
# cycle：循环迭代，如[1, 2, 3] -> 1, 2, 3, 1, 2, 3, 1, ...
from itertools import cycle

counter = 0
for item in cycle([1, 2, 3]):
    if counter > 6:
        break
    print(item, end=" ")  # 输出: 1 2 3 1 2 3 1
    counter += 1

######################################################################
# accumulate：用于求前缀和，如[1, 2, 3, 4] -> [0, 1, 3, 6, 10]
from itertools import accumulate

data = [1, 2, 3, 4]
result = list(accumulate(data, initial=0)) # 用于求前缀和
print(result)  # 输出: [0, 1, 3, 6, 10]

######################################################################
# combinations：用于求组合，如[1, 2, 3] -> [(1, 2), (1, 3), (2, 3)]
from itertools import combinations

data = [1, 2, 3]
result = list(combinations(data, 2))
print(result)  # 输出: [(1, 2), (1, 3), (2, 3)]

######################################################################
# permutations：用于求排列，如[1, 2, 3] -> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
from itertools import permutations

data = [1, 2, 3]
result = list(permutations(data, 2))
print(result)  # 输出: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

######################################################################
# islice：用于切片迭代器，如range(10) -> [2, 4, 6]
from itertools import islice

data = range(10)
result = list(islice(data, 2, 8, 2))
print(result)  # 输出: [2, 4, 6]

######################################################################
# groupby：用于分组，如[1, 1, 2, 2, 3, 3] -> [(1, [1, 1]), (2, [2, 2]), (3, [3, 3])]
from itertools import groupby

def height_class(h):
    if h > 180:
        return 'tall'
    elif h < 160:
        return 'short'
    else:
        return 'middle'

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
friends = sorted(friends, key=height_class)

for m, n in groupby(friends, key=height_class):
    print(m)
    print(list(n))

######################################################################
# count：用于生成一个无限序列，如count(10, 2) -> 10, 12, 14, 16, 18, 20
from itertools import count

for number in count(10, 2):
    if number > 20:
        break
    print(number, end=" ")  # 输出: 10 12 14 16 18 20

######################################################################
# filterfalse：用于过滤假值，如filterfalse(lambda x: x % 2, range(10)) -> [0, 2, 4, 6, 8]
from itertools import filterfalse

even_numbers = list(filterfalse(lambda x: x % 2, range(10)))
print(even_numbers)  # 输出: [0, 2, 4, 6, 8]

######################################################################
# dropwhile：用于丢弃元素，如dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]) -> [6, 4, 1]
from itertools import dropwhile

result = list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
print(result)  # 输出: [6, 4, 1]

######################################################################
# product：用于求笛卡尔积，如product('AB', '12') -> [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
from itertools import product

result = list(product('AB', '12'))
print(result)  # 输出: [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
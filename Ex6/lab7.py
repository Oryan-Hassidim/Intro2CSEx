
from types import FrameType
from typing import List


def up_and_right(n, k, lst, so_far=''):
    if n == 0 == k and so_far != '':
        lst.append(so_far)
        return
    if n > 0:
        up_and_right(n - 1, k, lst, so_far + 'u')
    if k > 0:
        up_and_right(n, k - 1, lst, so_far + 'r')



lst = []
up_and_right(1, 1, lst)
print(*lst, sep='\n', end='\n\n')

lst.clear()
up_and_right(1, 2, lst)
print(*lst, sep='\n', end='\n\n')

lst.clear()
up_and_right(2, 1, lst)
print(*lst, sep='\n', end='\n\n')

lst.clear()
up_and_right(2, 2, lst)
print(*lst, sep='\n', end='\n\n')

lst.clear()
up_and_right(1, 10, lst)
print(*lst, sep='\n', end='\n\n')


def count_sp_ways_core(x, n, so_far=None):
    if so_far is None:
        so_far = set()

    if x < 0:
        return 0
    if x == 0:
        return 1
    res = 0

    # for i in range(max(so_far | {0}) + 1, round(x ** (1/n)) + 1):
    #    if i not in so_far:
    #        res += count_sp_ways_core(x - i ** n, n, so_far | {i})

    def check(i):
        nonlocal res
        if i < max(so_far | {0}) + 1:
            return
        res += count_sp_ways_core(x - i ** n, n, so_far | {i})
        check(i - 1)

    check(round(x ** (1/n)) + 1)
    return res


def count_sp_ways(x, n):
    print(count_sp_ways_core(x, n))


count_sp_ways(1, 1)
count_sp_ways(100, 2)

#paren = {0: []}
paren = {0: ['']}


def all_options(l1: List[List], l2: List[List]):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    return [l1[i] + l2[j] for i in range(len(l1)) for j in range(len(l2))]


def map_map(f, l):
    return list(map(lambda x: list(map(f, x)), l))


def reduce_all_options(*lists):
    if lists == []:
        return []
    res = lists[0]
    for l in lists[1:]:
        res = list(all_options(res, l))
    return res


def find_paren_core(n, start):
    if n in paren:
        return map_map(lambda x: x + start, paren[n])
    res = []
    for i in range(n):
        res += reduce_all_options([[start]],
                                  find_paren_core(i, start + 1),
                                  [[start]],
                                  find_paren_core(n - i - 1, start + i + 1))
    paren[n] = map_map(lambda x: x - start, res)
    return res


def replace(lst, old, new):
    res = []
    flag = False
    for x in lst:
        if x == old and not flag:
            res.append(new[0])
            flag = True
        elif x == old:
            res.append(new[1])
        else:
            res.append(x)
    return res


def apply_paren(template,  pairs, i=0, res=None):
    if res is None:
        res = []
    if i * 2 == len(template):
        res.append(''.join(template))
        return res
    for pair in pairs:
        apply_paren(replace(template, i, pair), pairs,  i + 1, res)
    return res


print(*find_paren_core(3, 0), sep='\n')

print(apply_paren([0, 0], ["()"]))
print(apply_paren([0, 0], ["()", "{}", "[]"]))
print(apply_paren([0, 1, 1, 0], ["()", "{}"]))


def all_paren(n, pairs):
    templates = find_paren_core(n, 0)
    res = []
    for template in templates:
        res.extend(apply_paren(template, pairs,))
    return res


res = ['(())', '()()', '(){}', '({})', '{()}', '{{}}', '{}()', '{}{}']
print(res)
print(sorted(all_paren(2, ["()", "{}"])), end = "\n\n\n")
print(*sorted(all_paren(3, ["()", "{}", "[]"])), sep='\n', end = "\n\n\n")
print(*sorted(all_paren(4, ["()", "{}", "[]"])), sep='\n', end = "\n\n\n")
print(*sorted(all_paren(6, ["()", "{}", "[]"])), sep='\n', end = "\n\n\n")


def frac(n):
    if n == 0:
        return 1
    return n * frac(n - 1)

print(frac(10))
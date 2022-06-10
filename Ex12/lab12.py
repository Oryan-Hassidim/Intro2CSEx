# 1
def get_even_func():
    return lambda x: x%2==0

# 2
def minus_one_func():
    return lambda x: x-1

# 3
def my_pow(x):
    return lambda y:x**y

# 4
from functools import reduce
def count_appearances1(letter, word):
    fun = lambda n,c: n+1 if c==letter else n
    return reduce(fun, word, 0)
def count_appearances2(letter, word):
    fun = lambda c: 1 if c==letter else 0
    return sum(map(fun, word))
def count_appearances3(letter, word):
    fun = lambda c: c==letter
    return len(list(filter(fun, word)))


# 5
def last_in(x):
    x,last_in.l = last_in.l,x
    return x
last_in.l = None


#6
def dont_run_twice(f):
    f.last = None
    def inner(*args):
        if f.last == args:
            res = None
        else:
            res = f(*args)
        f.last = args
        return res
    return inner
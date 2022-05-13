import math

def num_permutations(word):
    return math.factorial(len(word))

def num_permutations(word):
    if word == "":
        return 1
    count = 0
    for c in word:
        count += num_permutations(word.replace(c, ""))
    return count

def num_different_permutations(word):
    if word == "":
        return 1
    count = 0
    options = set()
    for c in word:
        new_word = word.replace(c, "", 1)
        if new_word not in options:
            count += num_different_permutations(new_word)
            options.add(new_word)
    return count

def num_filtered_permutations(word, first = ""):
    if word == "":
        return 1
    count = 0
    options = set()
    for c in word:
        new_word = word.replace(c, "", 1)
        if new_word not in options and c != first:
            count += num_filtered_permutations(new_word, c)
            options.add(new_word)
    return count


funcs = []
for i in range(10):
    funcs.append(lambda: print(i))

for j in range(10):
    funcs[j]()

funcs = []
for i in range(10):
    temp = i
    funcs.append(lambda: print(temp))

for j in range(10):
    funcs[j]()


funcs = []
for i in range(10):
    temp = i
    funcs.append(lambda: print(temp))

for i in range(10):
    funcs[i]()


funcs = []
for i in range(10):
    funcs.append(lambda: print(i))

for i in range(10):
    funcs[i]()


funcs = []
for i in range(10):
    funcs.append(lambda: print(i))

for i in funcs:
    i()


m = map(lambda x,y: x*y, [0,1],(1,2))



def adding(n, current):
    if n == -1:
        return current
    current = adding(n-1, current)
    current.append(magic_list(n))
    return current

def magic_list(n):
    if n == 0:
        return []
    return adding(n-1, [])

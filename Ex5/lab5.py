
def function_to_test(s):
    return s == s[::-1]


import random


def generate_letter():
    return chr(random.randint(ord("A"), ord("z") + 1))


def generate_string(length):
    """Returns new string with different chars"""
    p = set(range(ord("A"), ord("z") + 1))
    s = ""
    for _ in range(length):
        c = chr(random.choice(list(p)))
        p -= {c}
        s += c
    return s


def testing():
    e = "Fail"
    f = function_to_test

    if f("") != True:
        return e
    if f(generate_letter()) != True:
        return e
    if f(generate_letter() * 2) != True:
        return e
    if f(generate_letter() * 3) != True:
        return e

    p = generate_letter() + generate_letter()
    p = p + p[::-1]
    if f(p) != True:
        return e
    p = generate_letter() + generate_letter()
    p = p + generate_letter() + p[::-1]
    if f(p) != True:
        return e

    if f("+-*/*-+") != True:
        return e
    if f("+-*//*-+") != True:
        return e
    if f("+-*/ /*-+") != True:
        return e

    if f(": ") != False:
        return e
    if f(generate_string(2)) != False:
        return e
    if f(generate_string(3)) != False:
        return e
    if f(generate_string(4)) != False:
        return e
    if f(generate_string(5)) != False:
        return e

    p = generate_string(random.randint(2, 10))
    p = p + p[::-1]
    if f(p) != True:
        return e
    p = generate_string(random.randint(2, 10))
    p = p + generate_letter() + p[::-1]
    if f(p) != True:
        return e
    p = generate_string(random.randint(2, 10))
    p = p + generate_letter() + p
    if f(p) != False:
        return e

    return "Success"


print(testing())



def function_to_test2(numbers_list):
    uniq_list = list(set(numbers_list))
    if len(uniq_list) > 1:
        return sorted(uniq_list)[-2]

def testing2():
    e = "Fail"
    f = function_to_test2
    
    if f([]) != None:
        return e
    
    n = random.randint(-500,500)
    if f([n]) != None:
        return e
    
    n = random.randint(-500,500)
    if f([n]*min(abs(n),2)) != None:
        return e
    if f([n]*min(abs(n+1),2)) != None:
        return e
    
    n = random.randint(-500,500)
    if f([n,n+1]) != n:
        return e

    n = random.randint(-500,500)
    l = [n,n+2,n+1]
    if f(l) != n+1:
        return e
    l += [n + 3]
    if f(l) != n+2:
        return e
    l += [n + 4]
    if f(l) != n+3:
        return e
    l += [n - 5]
    if f(l) != n+3:
        return e
    l.sort()
    if f(l) != n+3:
        return e
    l.sort(key = lambda x: -x)
    if f(l) != n+3:
        return e
    l.sort(key = lambda x: random.randint(-500,500))
    if f(l) != n+3:
        return e
    
    return "Success"
    
print(testing2())


def function_to_test3(list_of_lists):
    res_list = []
    if not len(list_of_lists):
        return res_list
    for item in list_of_lists[0]:
        for l in list_of_lists[1:]:
            if item not in l:
                break
        else:
            res_list.append(item)
    return res_list

def testing3():
    e = "Fail"
    f = function_to_test3
    
    if f([]) != []:
        return e
    for i in range(20):
        l = [[] for _ in range(random.randint(1,20))]
        if f(l) != []:
            return e

    n = random.randint(-500,500)
    l = [[n] for _ in range(random.randint(1,20))]
    if f(l) != [n]:
        return e
    
    n = random.randint(-500,500)
    l = [[n, n * 14] for _ in range(random.randint(1,20))]
    if set(f(l)) != {n, n * 14}:
        return e
    
    n = random.randint(-500,500)
    l = [[n] * random.randint(12,20) for _ in range(random.randint(1,20))]
    if set(f(l)) != {n}:
        return e
    
    l = [[1,1,2,3,4],
         [1,2,3],
         [1,2],
         [1]]
    
    if f(l) != [1]:
        return e

    
    return "Success"
    
        
    

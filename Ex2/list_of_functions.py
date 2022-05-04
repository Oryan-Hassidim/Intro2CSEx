
funcs = []
i = 0
while i < 10:
    funcs.append(lambda: print(i))
    i += 1

for x in funcs:
    x()

del(x)


funcs = []
for i in range(10):
    x = i
    funcs.append(lambda: print(x))
    

for x in funcs:
    x()

l = [x for x in range(10)]
funcs = map(lambda x: lambda: print(x),l)


for x in funcs:
    x()